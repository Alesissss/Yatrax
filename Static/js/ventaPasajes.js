// =============================================================================
// CONFIGURACIÓN Y CONSTANTES
// =============================================================================

const CONFIG = {
    MAX_ASIENTOS: 1,
    IGV: 0.18,
    TIEMPO_MAXIMO_COMPRA: 5, // En minutos
    RUTAS: {
        BUSCAR_VIAJES: '/ecommerce/home/buscarViajes',
        OBTENER_RUTAS: '/ecommerce/home/GetRutasConcatenadas',
        RENDERIZAR_ITINERARIO: '/ecommerce/home/renderizar_itinerario',
        OBTENER_DISENO_VEHICULO: '/ecommerce/home/obtener_diseno_vehiculo',
        API_PERSONA: '/ecommerce/home/api/get_persona_data',
        API_SUNAT: '/ecommerce/home/api/get_persona_data',
        METODOS: '/ecommerce/home/cargar_metodos',
        PROCESAR_PAGO: '/ecommerce/home/procesar_pago',
        PROCESAR_RESERVA: '/ecommerce/home/procesar_reserva',
        MARCAR_ASIENTO_OCUPADO: '/ecommerce/home/ocuparAsiento',
        MARCAR_ASIENTO_DISPONIBLE: '/ecommerce/home/liberarAsiento'
    },
    REGEX: {
        telefono: /^9\d{8}$/,
        dni: /^\d{8}$/,
        ruc: /^(10|20)\d{9}$/,
        pasaporte: /^[A-Z0-9]{6,12}$/i,
        ce: /^[A-Z0-9]{9,12}$/i,
        nombre: /^[\p{L} '-]{2,60}$/u,
        email: /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/,
        direccion: /^[a-zA-Z0-9\sáéíóúÁÉÍÓÚñÑ\-,.#°º()]{5,100}$/,
        apellido: /^[A-Za-zÁÉÍÓÚáéíóúÑñ]+(?:[ '\-][A-Za-zÁÉÍÓÚáéíóúÑñ]+)*$/,
        razonSocial: /^[A-Za-z0-9ÁÉÍÓÚáéíóúÑñ&\.\-,() ]{2,100}$/,
        positivos: /^[0-9]+(?:\.[0-9]+)?$/
    }
};

const SetearConfig = {
    async init() {
        await this.setDatos();
    },

    async setDatos() {
        try {
            const datosFetch = await this.getDatosFromBD();
            CONFIG.MAX_ASIENTOS = datosFetch.max_pasajes_venta;
            CONFIG.IGV = datosFetch.igv;
            CONFIG.TIEMPO_MAXIMO_COMPRA = datosFetch.tiempo_maximo_venta_minutos;
        } catch (error) {
            toastr.error("Error al cargar las configuraciones");
        }
    },

    async getDatosFromBD() {
        const response = await fetch("/ecommerce/home/GetConfGeneral");
        const data = await response.json();

        if (data.Status === 'success') {
            return data.data;
        }

        throw new Error(data.Msj || "Error al cargar configuraciones");
    }
};

// Funciones auxiliares para métodos de pago
async function obtenerNombreMetodo(idMetodo) {
    const response = await fetch(`/ecommerce/home/obtenerMetodoPagoxID/${idMetodo}`);
    return await response.text();
}

async function obtenerNombreTipoMetodo(idTipo) {
    const response = await fetch(`/ecommerce/home/obtenerTipoMetodoxID/${idTipo}`);
    return await response.text();
}

// =============================================================================
// ESTADO GLOBAL DE LA APLICACIÓN
// =============================================================================

const AppState = {
    currentStep: 0,
    maxStep: 0,
    itinerarioRegreso: null,

    setCurrentStep(step) {
        this.currentStep = step;
        if (step > this.maxStep) this.maxStep = step;
    },

    resetProgress() {
        this.currentStep = 0;
        this.maxStep = 0;
        this.itinerarioRegreso = null;
    }
};

// =============================================================================
// CLASE VENTA
// =============================================================================

class Venta {
    constructor(tipo_doc, numDoc, nombres, apellidoPaterno, apellidoMaterno, fechaNacimiento,
        telefono, seleccionSexo, sexo, correo, brazos, esMenor) {
        this.tipoDoc = tipo_doc;
        this.numDoc = numDoc;
        this.nombres = nombres;
        this.apellidoPaterno = apellidoPaterno;
        this.apellidoMaterno = apellidoMaterno;
        this.fechaNacimiento = fechaNacimiento;
        this.telefono = telefono;
        this.seleccionSexo = seleccionSexo;
        this.sexo = sexo;
        this.correo = correo;
        this.brazos = brazos;
        this.esMenor = esMenor;
    }

    static guardarEnStorage(idAsiento, venta) {
        const ventasGuardadas = JSON.parse(sessionStorage.getItem("ventas") || "{}");
        ventasGuardadas[idAsiento] = venta;
        sessionStorage.setItem("ventas", JSON.stringify(ventasGuardadas));
    }

    static obtenerDeStorage(idAsiento) {
        const ventasGuardadas = JSON.parse(sessionStorage.getItem("ventas") || "{}");
        return ventasGuardadas[idAsiento] || null;
    }
}

// =============================================================================
// VALIDADOR INTEGRADO Y MEJORADO
// =============================================================================

class Validator {
    static showError(input, msg, type = 'validation') {
        const errorClass = `error-msg-${type}`;
        let errorElement = input.parentNode.querySelector(`.${errorClass}`);

        if (!errorElement) {
            errorElement = document.createElement('small');
            errorElement.className = errorClass;
            errorElement.style.color = '#fc8181';
            input.insertAdjacentElement('afterend', errorElement);
        }

        errorElement.textContent = msg;
        errorElement.style.display = 'block';
        input.classList.add('manually-invalid');
    }

    static clearError(input, type = 'validation') {
        const errorClass = `error-msg-${type}`;
        const errorElement = input.parentNode.querySelector(`.${errorClass}`);

        if (errorElement) {
            errorElement.style.display = 'none';
        }

        input.classList.remove('manually-invalid');
    }

    static validateDocument(tipo, valor) {
        const validations = {
            '1': { regex: CONFIG.REGEX.dni, message: 'DNI debe tener 8 dígitos.' },
            '2': { regex: CONFIG.REGEX.ruc, message: 'RUC debe comenzar con 10 o 20 y tener 11 dígitos.' },
            '3': { regex: CONFIG.REGEX.ce, message: 'CE debe tener 9-12 caracteres alfanuméricos.' },
            '4': { regex: CONFIG.REGEX.pasaporte, message: 'Pasaporte debe tener 6-12 caracteres alfanuméricos.' }
        };

        const validation = validations[tipo];
        if (!validation) {
            return { valid: false, message: 'Seleccione tipo de documento.' };
        }

        return {
            valid: validation.regex.test(valor),
            message: validation.message
        };
    }

    static validatePhone(telefono) {
        return CONFIG.REGEX.telefono.test(telefono);
    }

    static validateEmail(email) {
        return CONFIG.REGEX.email.test(email);
    }

    static validateName(nombre) {
        return CONFIG.REGEX.nombre.test(nombre);
    }

    static validateAddress(direccion) {
        return CONFIG.REGEX.direccion.test(direccion);
    }

    static validatePositiveNumber(value) {
        return CONFIG.REGEX.positivos.test(value);
    }

    static validarRequeridos() {
        const contenedor = document.querySelector('.tabs-content');
        if (!contenedor) return true;

        const camposRequeridos = contenedor.querySelectorAll('input[required], select[required], textarea[required]');

        for (let campo of camposRequeridos) {
            const valor = campo.tagName.toLowerCase() === 'select'
                ? campo.value
                : campo.value.trim();

            if (!valor) {
                campo.style.borderColor = '#fc8181';
                campo.focus();
                return false;
            } else {
                campo.style.borderColor = '';
            }
        }

        return true;
    }

    // Validación de formulario completo
    static validateFormComplete(formSelector) {
        const form = document.querySelector(formSelector);
        if (!form) return false;

        const fields = form.querySelectorAll('input, select, textarea');
        let isValid = true;

        for (const field of fields) {
            if (field.offsetParent === null) continue; // Campo oculto
            if (field.type === 'radio') continue; // Validación especial para radios

            if (!field.value.trim()) {
                isValid = false;
                break;
            }
        }

        // Validar grupos de radio buttons
        const radioGroups = {};
        form.querySelectorAll('input[type="radio"]').forEach(radio => {
            if (radio.name) radioGroups[radio.name] = true;
        });

        for (const groupName in radioGroups) {
            const group = form.querySelectorAll(`input[type="radio"][name="${groupName}"]`);
            if (group.length && !Array.from(group).some(r => r.checked)) {
                isValid = false;
                break;
            }
        }

        return isValid;
    }

    // Validación en tiempo real
    static setupRealTimeValidation(formSelector) {
        const form = document.querySelector(formSelector);
        if (!form) return;

        form.addEventListener('input', (e) => {
            const field = e.target;
            this.validateField(field);
        });

        form.addEventListener('change', (e) => {
            const field = e.target;
            this.validateField(field);
        });
    }

    static validateField(field) {
        const value = field.value.trim();
        const type = field.type || 'text';
        let isValid = true;
        let message = '';

        // Validaciones básicas
        if (field.required && !value) {
            isValid = false;
            message = 'Este campo es obligatorio';
        } else if (value) {
            // Validaciones específicas por tipo
            switch (type) {
                case 'email':
                    if (!this.validateEmail(value)) {
                        isValid = false;
                        message = 'Email inválido';
                    }
                    break;
                case 'tel':
                    if (!this.validatePhone(value)) {
                        isValid = false;
                        message = 'Teléfono debe tener 9 dígitos';
                    }
                    break;
                case 'text':
                    if (field.name?.includes('nombre') || field.placeholder?.includes('nombre')) {
                        if (!this.validateName(value)) {
                            isValid = false;
                            message = 'Solo letras y espacios permitidos';
                        }
                    }
                    break;
            }
        }

        // Mostrar u ocultar error
        if (!isValid) {
            this.showError(field, message);
        } else {
            this.clearError(field);
        }

        return isValid;
    }
}
// =============================================================================
// GESTIÓN DE NAVEGACIÓN Y PESTAÑAS
// =============================================================================

const NavigationManager = {
    updateFormVisibility() {
        const form = document.getElementById('form-destino');
        const steps = document.querySelectorAll('.step');
        const tabs = document.querySelectorAll('.tab-link');

        if (form) {
            form.classList.toggle('hidden', AppState.currentStep === 3);
        }

        steps.forEach(step => step.classList.remove('active'));
        tabs.forEach(tab => tab.classList.remove('active', 'disabled'));

        if (steps[AppState.currentStep]) {
            steps[AppState.currentStep].classList.add('active');
        }
        if (tabs[AppState.currentStep]) {
            tabs[AppState.currentStep].classList.add('active');
        }

        this.controlarAccesoTabs();
    },

    controlarAccesoTabs() {
        const tabs = document.querySelectorAll('.tab-link');

        tabs.forEach(tab => {
            const stepIndex = parseInt(tab.getAttribute('data-step'));

            tab.classList.add('disabled');
            tab.setAttribute('disabled', 'true');
            tab.style.pointerEvents = 'none';

            if (this.puedeAccederATab(stepIndex)) {
                tab.classList.remove('disabled');
                tab.removeAttribute('disabled');
                tab.style.pointerEvents = 'auto';
            }
        });
    },

    puedeAccederATab(tabIndex) {
        switch (tabIndex) {
            case 0:
                return AppState.currentStep === 0;
            case 1:
                return AppState.currentStep === 1
            case 2:
                return AppState.currentStep === 2
            case 3:
                return AppState.currentStep === 3;
            default:
                return false;
        }
    },

    eligioItinerarioRegreso() {
        const fechaVuelta = $("input[name='fecha_vuelta']").val();
        return fechaVuelta && fechaVuelta.trim() !== '';  // Verifica si se ha elegido fecha de vuelta
    },

    tieneItinerarioRegreso() {
        return AppState.itinerarioRegreso && AppState.itinerarioRegreso.length > 0;  // Verifica si ya hay un itinerario de regreso cargado
    },

    async mostrarLoader(mensaje = "Cargando...") {
        const overlay = document.createElement('div');
        overlay.id = 'navigation-loader';
        overlay.style.cssText = `
            position: fixed; top: 0; left: 0; width: 100%; height: 100%;
            background: rgba(0,0,0,0.7); display: flex; justify-content: center;
            align-items: center; z-index: 9999;
        `;

        overlay.innerHTML = `
            <div style="text-align: center; color: white;">
                <div class="spinner-border text-light" style="width: 3rem; height: 3rem;"></div>
                <h5 class="mt-3">${mensaje}</h5>
            </div>
        `;

        document.body.appendChild(overlay);
        await new Promise(resolve => setTimeout(resolve, 800));
    },

    ocultarLoader() {
        const loader = document.getElementById('navigation-loader');
        if (loader) loader.remove();
    },

    async goToNextStep(mensaje = "Cargando...") {
        if (AppState.currentStep < 3) {
            await this.mostrarLoader(mensaje);
            AppState.setCurrentStep(AppState.currentStep + 1);
            this.updateFormVisibility();
            this.ocultarLoader();
        }
    },

    async goToStep(stepIndex, mensaje = "Cargando...") {
        if (this.puedeAccederATab(stepIndex)) {
            if (stepIndex !== AppState.currentStep) {
                await this.mostrarLoader(mensaje);
                AppState.currentStep = stepIndex;
                this.updateFormVisibility();
                this.ocultarLoader();
            }
        } else {
            toastr.warning("No puedes acceder a esta sección en este momento.");
        }
    },

    async procesarBusqueda() {
        await this.mostrarLoader("Buscando viajes disponibles...");
        AppState.setCurrentStep(1);
        AppState.maxStep = Math.max(AppState.maxStep, 1);
        this.updateFormVisibility();
        this.ocultarLoader();
    },

    async confirmarDatosIda() {
        if (!this.validarDatosPasajerosCompletos()) {
            toastr.error("Complete los datos de todos los pasajeros antes de continuar");
            return;
        }

        const confirmacion = await Swal.fire({
            title: '¿Todos los datos son correctos?',
            text: 'Verifica que toda la información de los pasajeros esté completa y sea correcta.',
            icon: 'question',
            showCancelButton: true,
            confirmButtonText: 'Sí, continuar',
            cancelButtonText: 'Revisar datos',
            confirmButtonColor: '#28a745',
            cancelButtonColor: '#6c757d',
            reverseButtons: true
        });

        if (!confirmacion.isConfirmed) return;

        const fechaVuelta = $("input[name='fecha_vuelta']").val();

        if (!fechaVuelta?.trim()) {
            await this.irAPago();
            return;
        }
        let itinerarioVacio = !AppState.itinerarioRegreso?.length

        await this.irAItinerarioRegreso(itinerarioVacio);
    },

    async confirmarDatosRegreso() {
        if (!this.validarDatosPasajerosCompletos()) {
            toastr.error("Complete los datos de todos los pasajeros antes de continuar");
            return;
        }

        const confirmacion = await Swal.fire({
            title: '¿Todos los datos son correctos?',
            text: 'Verifica que toda la información de los pasajeros esté completa y sea correcta.',
            icon: 'question',
            showCancelButton: true,
            confirmButtonText: 'Sí, ir al pago',
            cancelButtonText: 'Revisar datos',
            confirmButtonColor: '#28a745',
            cancelButtonColor: '#6c757d',
            reverseButtons: true
        });

        if (confirmacion.isConfirmed) {
            await this.irAPago();
        }
    },
    soloIrAPago(){

    },

    async irAItinerarioRegreso(itinerarioVacio) {
        await this.mostrarLoader("Cargando itinerario de regreso...");
        AppState.setCurrentStep(2);
        AppState.maxStep = Math.max(AppState.maxStep, 2);

        setTimeout(() => {
            ItineraryManager.cargarItinerario(AppState.itinerarioRegreso, 'contenedor_viajes_vuelta', 'vuelta', itinerarioVacio);
        }, 100);

        this.updateFormVisibility();
        this.ocultarLoader();
    },

    async irAPago() {
        await this.mostrarLoader("Preparando información de pago...");
        AppState.setCurrentStep(3);
        AppState.maxStep = Math.max(AppState.maxStep, 3);

        setTimeout(() => {
            if (typeof PaymentManager !== 'undefined') {
                PaymentManager.initialize();
            }
        }, 100);

        this.updateFormVisibility();
        this.ocultarLoader();
    },

    validarDatosPasajerosCompletos() {
        const ventas = JSON.parse(sessionStorage.getItem("ventas") || "{}");

        if (Object.keys(ventas).length === 0) {
            toastr.warning("No hay asientos seleccionados");
            return false;
        }

        const camposObligatorios = ['numDoc', 'nombres', 'apellidoPaterno', 'apellidoMaterno', 'telefono', 'correo'];

        for (const asientoId in ventas) {
            const venta = ventas[asientoId];

            for (const campo of camposObligatorios) {
                if (!venta[campo]?.trim()) {
                    toastr.warning(`Complete los datos del pasajero en el asiento ${asientoId}`);
                    return false;
                }
            }
        }

        return true;
    },

    async volverAItinerarioIda() {
        const confirmacion = await Swal.fire({
            title: '¿Volver al itinerario de ida?',
            text: 'Podrás modificar tu selección de asientos y datos de pasajeros.',
            icon: 'question',
            showCancelButton: true,
            confirmButtonText: 'Sí, volver',
            cancelButtonText: 'Cancelar',
            confirmButtonColor: '#17a2b8',
            cancelButtonColor: '#6c757d',
            reverseButtons: true
        });

        if (confirmacion.isConfirmed) {
            await this.goToStep(1, "Cargando itinerario de ida...");
        }
    },

    initializeTabEvents() {
        document.querySelectorAll('.tab-link').forEach(tab => {
            tab.addEventListener('click', (event) => {
                const stepIndex = parseInt(tab.getAttribute('data-step'));

                if (!this.puedeAccederATab(stepIndex)) {
                    event.preventDefault();
                    toastr.warning("No puedes acceder a esta sección en este momento.");
                    return;
                }

                this.goToStep(stepIndex);
            });
        });
    },

    inicializarEstadoPorDefecto() {
        AppState.currentStep = 0;
        AppState.maxStep = 0;
        AppState.itinerarioRegreso = null;
        this.updateFormVisibility();
    }
};

// =============================================================================
// GESTIÓN DE BÚSQUEDA Y DATOS
// =============================================================================

const SearchManager = {
    capturarDatos() {
        const texto = $('#cbx_Ciudades').select2('data')[0].text.split(' - ');
        return {
            origen: texto[0],
            destino: texto[1],
            fecha_ida: $("input[name='fecha_ida']").val(),
            fecha_vuelta: $("input[name='fecha_vuelta']").val()
        };
    },

    validarDatos() {
        const ruta = $('#cbx_Ciudades').val();
        const ida = $('input[name="fecha_ida"]').val();

        if (!ruta || !ida) {
            toastr.warning("Debes completar origen, destino y fecha de ida.");
            return false;
        }
        return true;
    },

    async buscarYMostrarItinerario() {
        if (!this.validarDatos()) return;

        const hayProgreso = this.verificarProgreso();

        if (hayProgreso) {
            const confirmacion = await Swal.fire({
                title: "¿Realizar nueva búsqueda?",
                text: "Esta acción eliminará tu progreso actual, ¿estás seguro de hacerlo?",
                icon: "warning",
                showCancelButton: true,
                confirmButtonText: "Sí, buscar",
                cancelButtonText: "Cancelar",
                confirmButtonColor: '#d33',
                cancelButtonColor: '#6c757d',
                reverseButtons: true,
            });

            if (!confirmacion.isConfirmed) return;

            await this.limpiarDatosPreviosCompleto();
        }

        await this.ejecutarBusqueda();
    },

    verificarProgreso() {
        const hayAsientosSeleccionados = SeatManager?.asientosSeleccionados?.size > 0;
        const ventasStorage = sessionStorage.getItem('ventas');
        const hayVentas = ventasStorage && Object.keys(JSON.parse(ventasStorage)).length > 0;

        return hayAsientosSeleccionados || hayVentas;
    },

    async limpiarDatosPreviosCompleto() {
        try {
            if (SeatManager.asientosSeleccionados.size > 0) {
                await SeatManager.liberarTodosLosAsientos();
            }

            await this.liberarAsientosDesdeStorage();
            App.resetearSistemaCompleto();
        } catch (error) {
            App.resetearSistemaCompleto();
        }
    },

    async liberarAsientosDesdeStorage() {
        const ventasStorage = sessionStorage.getItem('ventas');
        if (!ventasStorage) return;

        try {
            const ventas = JSON.parse(ventasStorage);
            const asientosEnStorage = Object.keys(ventas);

            if (asientosEnStorage.length > 0) {
                const promesasLiberacion = asientosEnStorage.map(asientoId =>
                    SeatManager.marcarAsientoComoDisponible(asientoId)
                );

                await Promise.allSettled(promesasLiberacion);
            }
        } catch (error) {
            // Error manejado silenciosamente
        }
    },

    async ejecutarBusqueda() {
        const datos = this.capturarDatos();
        App.resetearSistemaCompletoSinRutas();

        return new Promise((resolve, reject) => {
            $.ajax({
                url: CONFIG.RUTAS.BUSCAR_VIAJES,
                data: datos,
                method: 'POST',
                success: (resp) => {
                    this.procesarRespuestaBusqueda(resp);
                    resolve(resp);
                },
                error: (xhr, status, error) => {
                    toastr.error("Error en la conexión al servidor.");
                    reject(error);
                }
            });
        });
    },

    async procesarRespuestaBusqueda(resp) {
        if (resp.Status !== 'success') {
            toastr.warning('ERROR AL BUSCAR EL VIAJE: ' + resp.Msj);
            return;
        }

        if (!resp.data_ida || resp.data_ida.length === 0) {
            AppState.setCurrentStep(0); // Cambiar a paso 0
            NavigationManager.updateFormVisibility();
            toastr.warning("No se han encontrado viajes para esas fechas");
            return;
        }

        ItineraryManager.cargarItinerario(resp.data_ida, 'contenedor_viajes_ida', 'ida');

        AppState.itinerarioRegreso = resp.data_vuelta || null;
        await NavigationManager.procesarBusqueda();
        toastr.success('VIAJES ENCONTRADOS CORRECTAMENTE');
    }
};

// =============================================================================
// GESTIÓN DE RUTAS Y FECHAS
// =============================================================================

const RouteManager = {
    cargarRutas() {
        $.getJSON(CONFIG.RUTAS.OBTENER_RUTAS, (response) => {
            if (response.Status === 'success') {
                this.configurarSelect2ConDatos(response.data);
            } else {
                this.configurarSelect2Vacio();
            }
        });
    },

    configurarSelect2ConDatos(data) {
        const items = data.map((item, index) => ({
            id: index,
            text: item.ruta
        }));

        $('#cbx_Ciudades').empty().select2({
            width: '100%',
            theme: 'bootstrap4',
            placeholder: "Buscar...",
            data: items,
            language: { noResults: () => "No se encontraron resultados" },
            allowClear: true
        }).trigger('change');
    },

    configurarSelect2Vacio() {
        $('#cbx_Ciudades').html('<option disabled>-- No hay rutas disponibles --</option>')
            .select2({
                width: '100%',
                theme: 'bootstrap4',
                minimumResultsForSearch: Infinity,
                allowClear: false
            });
    },

    formatearFechas() {
        const hoyLocal = new Date().toLocaleDateString('en-CA');
        const ida = $('input[name="fecha_ida"]');
        const vuelta = $('input[name="fecha_vuelta"]');

        ida.attr('min', hoyLocal);
        ida.on('change', function () {
            const valIda = $(this).val();
            if (vuelta.val() && vuelta.val() < valIda) {
                vuelta.val('');
            }
            vuelta.removeAttr('disabled').attr('min', valIda);
        });
    }
};

// =============================================================================
// GESTIÓN DE ITINERARIOS
// =============================================================================

const ItineraryManager = {
    async cargarItinerario(itinerarios, contenedorId, sufijo, itinerarioVacio = false) {
        const contenedor = document.getElementById(contenedorId);
        contenedor.innerHTML = '';
        if (itinerarioVacio) {
            contenedor.innerHTML = `
        <div class="alert alert-warning text-center">
            <i class="fas fa-exclamation-triangle"></i> 
            <strong>No se encontraron viajes para esa fecha</strong>
        </div>
        <div class="d-grid gap-2 mt-3">
            <button class="btn btn-outline-secondary" onclick="volverAItinerarioIda()">
              <i class="fas fa-arrow-left"></i> Volver a ida
            </button>
            <button class="btn btn-outline-primary" onclick='acabarSegundoItinerario()'>
              <i class="fas fa-credit-card"></i> Ir al pago
            </button>
          </div>
        `;
            return;
        }

        try {
            const response = await fetch(CONFIG.RUTAS.RENDERIZAR_ITINERARIO, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ itinerarios, sufijo })
            });

            const data = await response.json();
            contenedor.innerHTML = data.html;

            setTimeout(() => {
                this.inicializarEventosPostRender(sufijo);
            }, 200);

        } catch (err) {
            toastr.error("Error al renderizar el itinerario: " + (err.message || err));
        }
    },

    inicializarEventosPostRender(sufijo) {
        ReniecAPI.initialize();
        this.configurarFuncionalidadElegir(sufijo);
    },

    configurarFuncionalidadElegir(sufijo) {
        document.addEventListener('click', (event) => {
            if (event.target.classList.contains(`mostrarContenido_${sufijo}`)) {
                const btn = event.target;
                event.stopPropagation();
                VehicleLayoutManager.generarMatrices(btn.id, sufijo);
            }
        });

        document.querySelectorAll(`.mostrarContenido_${sufijo}`).forEach(btn => {
            const targetId = btn.getAttribute('data-bs-target');
            const target = document.querySelector(targetId);

            if (target) {
                target.addEventListener('shown.bs.collapse', () => {
                    setTimeout(() => {
                        SeatManager.inicializarSeleccionAsientos(sufijo);
                        TimerManager.iniciar(CONFIG.TIEMPO_MAXIMO_COMPRA * 60, sufijo);
                        VehicleLayoutManager.restaurarEstadoAsientos(sufijo);
                    }, 150);
                });

                target.addEventListener('hidden.bs.collapse', () => {
                    TimerManager.detener(sufijo);
                });
            }
        });
    },

    validarDatosPasajerosCompletos() {
        const ventas = JSON.parse(sessionStorage.getItem("ventas") || "{}");

        if (Object.keys(ventas).length === 0) {
            toastr.warning("No hay asientos seleccionados");
            return false;
        }

        const camposObligatorios = ['numDoc', 'nombres', 'apellidoPaterno', 'apellidoMaterno', 'telefono', 'correo'];

        for (const asientoId in ventas) {
            const venta = ventas[asientoId];

            for (const campo of camposObligatorios) {
                if (!venta[campo]?.trim()) {
                    toastr.warning(`Complete los datos del pasajero en el asiento ${asientoId}`);
                    return false;
                }
            }
        }

        return true;
    }
};

// =============================================================================
// GESTIÓN DE DISEÑO DEL VEHÍCULO
// =============================================================================

const VehicleLayoutManager = {
    columnas: { "1": "", "2": "" },
    filas: { "1": "", "2": "" },

    async generarMatrices(idBoton, sufijo) {
        try {
            const response = await fetch(CONFIG.RUTAS.OBTENER_DISENO_VEHICULO, {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ id_dv: idBoton })
            });

            const res = await response.json();
            const datos = res.data;
            const niveles = res.niveles;

            niveles.forEach(dict => {
                this.columnas[`${dict.nroPiso}`] = dict.x;
                this.filas[`${dict.nroPiso}`] = dict.y;
            });

            const datosPiso1 = datos.filter(d => d.nroPiso == 1);
            const datosPiso2 = datos.filter(d => d.nroPiso == 2);

            this.generarMatrizDesdeDatos(datosPiso1, 1, `${idBoton}_${sufijo}`, sufijo);

            const contenedorPiso2 = document.getElementById(`contenedor_piso_2_${idBoton}_${sufijo}`);
            if (datosPiso2.length > 0) {
                contenedorPiso2.style.display = 'block';
                this.generarMatrizDesdeDatos(datosPiso2, 2, `${idBoton}_${sufijo}`, sufijo);
            } else {
                contenedorPiso2.style.display = 'none';
            }

            this.restaurarEstadoAsientos(sufijo);

        } catch (error) {
            toastr.error("Error al cargar el diseño del vehículo");
        }
    },

    generarMatrizDesdeDatos(datos, piso, sufijo, tipoItinerario) {
        const contenedor = document.getElementById(`matrizContainer_${piso}_${sufijo}`);
        if (!contenedor) return;

        contenedor.innerHTML = '';
        this.configurarEstilosMatriz(contenedor, piso);

        for (let y = 1; y <= this.filas[`${piso}`]; y++) {
            for (let x = 1; x <= this.columnas[`${piso}`]; x++) {
                const btn = this.crearElementoMatriz(datos, x, y, tipoItinerario);
                contenedor.appendChild(btn);
            }
        }
    },

    configurarEstilosMatriz(contenedor, piso) {
        Object.assign(contenedor.style, {
            display: 'grid',
            gridTemplateColumns: `repeat(${this.columnas[piso]}, 40px)`,
            gridTemplateRows: `repeat(${this.filas[piso]}, 40px)`,
            padding: '10px',
            margin: '0 auto',
            width: 'max-content',
            justifyContent: 'center',
            border: "2px solid #000"
        });
    },

    crearElementoMatriz(datos, x, y, tipoItinerario) {
        const dato = datos.find(d =>
            parseInt(d.x_dimension) === x && parseInt(d.y_dimension) === y
        );

        const btn = document.createElement('button');
        Object.assign(btn.style, { width: '40px', height: '40px' });
        btn.setAttribute('data-x', x);
        btn.setAttribute('data-y', y);

        if (dato) {
            this.configurarElementoConDatos(btn, dato, tipoItinerario);
        } else {
            this.configurarElementoVacio(btn);
        }

        return btn;
    },

    configurarElementoConDatos(btn, dato, tipoItinerario) {
        btn.id = dato.id_asiento ?? '';
        btn.setAttribute('data-tipo', dato.tipo_herramienta);
        btn.style.cursor = 'pointer';

        if (dato.tipo_herramienta === 1) {
            const estaSeleccionadoLocalmente = SeatManager.asientosSeleccionados.has(dato.id_asiento);

            if (estaSeleccionadoLocalmente) {
                btn.className = 'border border-dark border-2 asiento-seleccionado';
                btn.style.backgroundColor = '#28a745';
                btn.style.color = 'white';
                btn.innerText = dato.nombre;
            } else if (dato.estado === 1) {
                btn.className = 'border border-dark border-2 bg-white';
                btn.innerText = dato.nombre;
            } else {
                btn.className = 'border border-dark border-2 bg-dark text-white';
                btn.innerText = dato.nombre;
                btn.style.cursor = 'not-allowed';
                btn.disabled = true;
                btn.title = 'Asiento ocupado';
            }
        } else {
            this.configurarElementoHerramienta(btn, dato);
        }
    },

    configurarElementoVacio(btn) {
        Object.assign(btn.style, {
            border: 'none',
            background: 'transparent',
            cursor: 'default'
        });
        btn.disabled = true;
    },

    configurarElementoHerramienta(btn, dato) {
        Object.assign(btn.style, {
            border: 'none',
            background: 'transparent',
            cursor: 'default'
        });
        btn.disabled = true;
        btn.innerHTML = this.obtenerIcono(dato.icono);
    },

    obtenerIcono(icono) {
        return `<img src="/Static/${icono}" width="32" height="32" style="display: block; margin: auto;" alt="icono">`;
    },

    restaurarEstadoAsientos(sufijo) {
        SeatManager.asientosSeleccionados.forEach(asientoId => {
            const btnAsiento = document.getElementById(asientoId);
            if (btnAsiento && btnAsiento.getAttribute('data-tipo') === '1') {
                btnAsiento.classList.add("asiento-seleccionado");
                btnAsiento.style.backgroundColor = '#28a745';
                btnAsiento.style.color = 'white';
            }
        });

        setTimeout(() => {
            SeatManager.inicializarSeleccionAsientos(sufijo);
        }, 100);
    }
};

// =============================================================================
// GESTIÓN DE ASIENTOS
// =============================================================================

const SeatManager = {
    asientosSeleccionados: new Set(),

    inicializarSeleccionAsientos(sufijo) {
        const asientosPrevios = document.querySelectorAll(`[data-tipo="1"][data-listener-${sufijo}="true"]`);
        asientosPrevios.forEach(btn => {
            btn.removeAttribute(`data-listener-${sufijo}`);
        });

        const asientos = document.querySelectorAll('[data-tipo="1"]');
        if (asientos.length === 0) return;

        let asientosConfigurados = 0;

        asientos.forEach(btn => {
            const yaConfigurado = btn.getAttribute(`data-listener-${sufijo}`) === 'true';

            if (!btn.disabled && !yaConfigurado) {
                btn.setAttribute(`data-listener-${sufijo}`, 'true');

                const nuevoBtn = btn.cloneNode(true);
                btn.parentNode.replaceChild(nuevoBtn, btn);

                nuevoBtn.addEventListener('click', (event) => {
                    this.manejarClickAsiento(event, sufijo);
                });

                asientosConfigurados++;
            }
        });

        this.restaurarEstadoVisualAsientos(sufijo);
    },

    restaurarEstadoVisualAsientos(sufijo) {
        this.asientosSeleccionados.forEach(asientoId => {
            const btnAsiento = document.getElementById(asientoId);
            if (btnAsiento && btnAsiento.getAttribute('data-tipo') === '1') {
                if (!btnAsiento.classList.contains("asiento-seleccionado")) {
                    btnAsiento.classList.add("asiento-seleccionado");
                    btnAsiento.style.backgroundColor = '#28a745';
                    btnAsiento.style.color = 'white';
                }

                const contenedor = document.getElementById(`contenido_datos_${sufijo}`);
                if (contenedor && contenedor.classList.contains("d-none")) {
                    contenedor.classList.remove("d-none");
                }
            }
        });
    },

    async liberarTodosLosAsientos() {
        const promesasLiberacion = [];
        const asientosParaLiberar = [...this.asientosSeleccionados];

        for (const asientoId of asientosParaLiberar) {
            promesasLiberacion.push(
                this.marcarAsientoComoDisponible(asientoId)
                    .catch(error => ({ asientoId, error }))
            );
        }

        const ventas = JSON.parse(sessionStorage.getItem("ventas") || "{}");
        for (const asientoId in ventas) {
            if (!this.asientosSeleccionados.has(asientoId)) {
                promesasLiberacion.push(
                    this.marcarAsientoComoDisponible(asientoId)
                        .catch(error => ({ asientoId, error }))
                );
            }
        }

        if (promesasLiberacion.length > 0) {
            await Promise.allSettled(promesasLiberacion);
        }

        this.asientosSeleccionados.clear();
    },

    async manejarClickAsiento(event, sufijo) {
        const btn = event.target;
        const nombreAsiento = btn.innerText.trim();
        const asientoId = btn.id;
        const accordionItemId = `collapse-${btn.id}-${sufijo}`;

        if (btn.classList.contains("asiento-seleccionado")) {
            await this.deseleccionarAsiento(btn, nombreAsiento, accordionItemId, asientoId, sufijo);
            return;
        }

        if (!this.puedeSeleccionarAsiento()) {
            toastr.warning(`Solo puedes seleccionar hasta ${CONFIG.MAX_ASIENTOS} asientos.`);
            return;
        }

        const ocupadoExitoso = await this.marcarAsientoComoOcupado(asientoId);
        if (!ocupadoExitoso) {
            toastr.error("Error al reservar el asiento. Intente nuevamente.");
            return;
        }

        this.seleccionarAsiento(btn, nombreAsiento, accordionItemId, sufijo);
    },

    async marcarAsientoComoOcupado(asientoId) {
        try {
            const response = await fetch(CONFIG.RUTAS.MARCAR_ASIENTO_OCUPADO, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ asiento_id: asientoId })
            });

            const resultado = await response.json();
            return resultado.status === 1;
        } catch (error) {
            return false;
        }
    },

    async marcarAsientoComoDisponible(asientoId) {
        try {
            const response = await fetch(CONFIG.RUTAS.MARCAR_ASIENTO_DISPONIBLE, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ asiento_id: asientoId })
            });

            const resultado = await response.json();
            return resultado.status === 1;
        } catch (error) {
            return false;
        }
    },

    async deseleccionarAsiento(btn, nombreAsiento, accordionItemId, asientoId, sufijo) {
        const confirm = await Swal.fire({
            title: '¿Deseas quitar este asiento?',
            text: `Se eliminarán los datos ingresados para el asiento ${nombreAsiento}.`,
            icon: 'warning',
            showCancelButton: true,
            confirmButtonText: 'Sí, eliminar',
            cancelButtonText: 'Cancelar',
            reverseButtons: true
        });

        if (confirm.isConfirmed) {
            await this.marcarAsientoComoDisponible(asientoId);

            this.asientosSeleccionados.delete(asientoId);

            btn.classList.remove("asiento-seleccionado");
            btn.className = 'border border-dark border-2 bg-white';
            btn.innerText = nombreAsiento;
            btn.style.backgroundColor = '';
            btn.style.color = '';
            btn.style.cursor = 'pointer';
            btn.disabled = false;

            const accordionItem = document.getElementById(accordionItemId)?.closest(".accordion-item");
            if (accordionItem) accordionItem.remove();

            const ventas = JSON.parse(sessionStorage.getItem("ventas") || "{}");
            delete ventas[asientoId];
            sessionStorage.setItem("ventas", JSON.stringify(ventas));

            const accordion = document.getElementById(`accordionPasajeros_${sufijo}`);
            if (accordion && accordion.children.length === 0) {
                const contenedor = document.getElementById(`contenido_datos_${sufijo}`);
                if (contenedor) contenedor.classList.add("d-none");
            }

            toastr.success(`Asiento ${nombreAsiento} deseleccionado`);
        }
    },

    puedeSeleccionarAsiento() {
        return this.asientosSeleccionados.size < CONFIG.MAX_ASIENTOS;
    },

    seleccionarAsiento(btn, nombreAsiento, accordionItemId, sufijo) {
        this.asientosSeleccionados.add(btn.id);

        btn.classList.add("asiento-seleccionado");
        btn.style.backgroundColor = '#28a745';
        btn.style.color = 'white';

        const contenedor = document.getElementById(`contenido_datos_${sufijo}`);
        if (contenedor && contenedor.classList.contains("d-none")) {
            contenedor.classList.remove("d-none");
        }

        if (!document.getElementById(accordionItemId)) {
            this.crearFormularioAsiento(btn, nombreAsiento, accordionItemId, sufijo);
        }

        toastr.success(`Asiento ${nombreAsiento} seleccionado`);
    },

    crearFormularioAsiento(btn, nombreAsiento, accordionItemId, sufijo) {
        const accordion = document.getElementById(`accordionPasajeros_${sufijo}`);
        const headerId = `heading-${btn.id}-${sufijo}`;
        const isFirstAccordion = accordion.children.length === 0;

        const nuevoForm = document.createElement("div");
        nuevoForm.classList.add("accordion-item");
        nuevoForm.innerHTML = this.generarAcordeonPasajeros(
            headerId, accordionItemId, btn.id, nombreAsiento, isFirstAccordion, sufijo
        );

        accordion.appendChild(nuevoForm);
        ReniecAPI.initializeForSeat(btn.id);
        this.configurarValidacionFormulario(btn.id, sufijo);
    },

    configurarValidacionFormulario(asientoId, sufijo) {
        const camposObligatorios = [
            `numeroDocNuevo_${asientoId}`, `nombres_${asientoId}`,
            `apellidoPaterno_${asientoId}`, `apellidoMaterno_${asientoId}`,
            `fechaNacimientoNuevo_${asientoId}`, `telefono_${asientoId}`, `correo_${asientoId}`
        ];

        camposObligatorios.forEach(campoId => {
            const campo = document.getElementById(campoId);
            if (campo) {
                campo.addEventListener('input', () => {
                    this.validarFormularioCompleto(asientoId);
                    this.validarCampoEnTiempoReal(campoId);
                });
            }
        });

        const radioMasculino = document.getElementById(`sexoMasculino_${asientoId}`);
        const radioFemenino = document.getElementById(`sexoFemenino_${asientoId}`);

        if (radioMasculino) radioMasculino.addEventListener('change', () => this.validarFormularioCompleto(asientoId));
        if (radioFemenino) radioFemenino.addEventListener('change', () => this.validarFormularioCompleto(asientoId));
    },

    validarCampoEnTiempoReal(campoId) {
        const campo = document.getElementById(campoId);
        if (!campo) return;

        const valor = campo.value.trim();
        let esValido = true;
        let mensaje = "";

        if (campoId.includes('numeroDocNuevo_')) {
            const tipoDocSelect = document.getElementById(campoId.replace('numeroDocNuevo_', 'tipo_doc_'));
            const tipoDoc = tipoDocSelect ? tipoDocSelect.value : 'DNI';

            if (tipoDoc === 'DNI') {
                esValido = /^\d{8}$/.test(valor);
                mensaje = "DNI debe tener 8 dígitos";
            } else if (tipoDoc === 'CE') {
                esValido = /^\d{9,12}$/.test(valor);
                mensaje = "CE debe tener entre 9 y 12 dígitos";
            }
        } else if (campoId.includes('correo_')) {
            esValido = /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(valor);
            mensaje = "Formato de correo inválido";
        } else if (campoId.includes('telefono_')) {
            esValido = /^\d{9}$/.test(valor);
            mensaje = "Teléfono debe tener 9 dígitos";
        } else if (campoId.includes('nombres_') || campoId.includes('apellido')) {
            esValido = valor.length >= 2;
            mensaje = "Debe tener al menos 2 caracteres";
        } else if (campoId.includes('fechaNacimiento')) {
            esValido = valor !== '';
            mensaje = "Seleccione una fecha";
        }

        if (!esValido && valor) {
            Validator.showError(campo, mensaje);
        } else {
            Validator.clearError(campo);
        }
    },

    validarFormularioCompleto(asientoId) {
        const camposObligatorios = [
            `tipo_doc_${asientoId}`, `numeroDocNuevo_${asientoId}`, `nombres_${asientoId}`,
            `apellidoPaterno_${asientoId}`, `apellidoMaterno_${asientoId}`,
            `fechaNacimientoNuevo_${asientoId}`, `telefono_${asientoId}`, `correo_${asientoId}`
        ];

        let todosCompletos = true;

        for (const campoId of camposObligatorios) {
            const campo = document.getElementById(campoId);
            if (!campo || !campo.value.trim()) {
                todosCompletos = false;
                break;
            }
        }

        const masculino = document.getElementById(`sexoMasculino_${asientoId}`);
        const femenino = document.getElementById(`sexoFemenino_${asientoId}`);

        if (!masculino?.checked && !femenino?.checked) {
            todosCompletos = false;
        }

        const botonGuardar = document.querySelector(`button[onclick*="FormManager.enviarDatosPasajero"][onclick*="${asientoId}"]`);

        if (todosCompletos) {
            if (botonGuardar) {
                botonGuardar.disabled = false;
                botonGuardar.className = 'btn btn-outline-primary w-100';
                botonGuardar.innerHTML = 'Guardar datos';
            }
        } else {
            if (botonGuardar) {
                botonGuardar.disabled = true;
                botonGuardar.className = 'btn btn-secondary w-100';
                botonGuardar.innerHTML = 'Complete todos los campos';
            }
        }

        return todosCompletos;
    },

    generarAcordeonPasajeros(headerId, accordionItemId, btnId, nombreAsiento, isFirstAccordion, sufijo) {
        return `
            <h2 class="accordion-header" id="${headerId}">
                <button class="accordion-button ${!isFirstAccordion ? 'collapsed' : ''}" 
                        type="button" data-bs-toggle="collapse" 
                        data-bs-target="#${accordionItemId}" 
                        aria-expanded="${isFirstAccordion}"
                        aria-controls="${accordionItemId}">
                    Asiento: ${nombreAsiento}   
                </button>
            </h2>
            <div id="${accordionItemId}" 
                 class="accordion-collapse collapse ${isFirstAccordion ? 'show' : ''}" 
                 aria-labelledby="${headerId}" 
                 data-bs-parent="#accordionPasajeros_${sufijo}">
                <div class="accordion-body">
                    ${FormManager.generarFormularioHTML(nombreAsiento, btnId)}
                </div>
            </div>
        `;
    }
};

// =============================================================================
// GESTIÓN DE FORMULARIOS
// =============================================================================

const FormManager = {
    generarFormularioHTML(asientoNombre, asientoId) {
        return `
            <select class="form-select mb-2" id="tipo_doc_${asientoId}" required>
                <option value="DNI">DNI</option>
                <option value="CE">CE</option>
            </select>
            <input class="form-control mb-2" id="numeroDocNuevo_${asientoId}" placeholder="N° Documento" required>
            <input class="form-control mb-2" id="nombres_${asientoId}" placeholder="Nombres" required>
            <input class="form-control mb-2" id="apellidoPaterno_${asientoId}" placeholder="Apellido paterno" required>
            <input class="form-control mb-2" id="apellidoMaterno_${asientoId}" placeholder="Apellido materno" required>
            <input class="form-control mb-2" id="fechaNacimientoNuevo_${asientoId}" type="date" placeholder="Fecha nacimiento" required>
            <input class="form-control mb-2" id="telefono_${asientoId}" placeholder="Teléfono" type="tel" required>
            <div class="mb-2">
                <label class="me-2">Sexo:</label>
                <input type="radio" class="form-check-input" name="sexo-${asientoId}" id="sexoMasculino_${asientoId}" value="M" required> 
                <label for="sexoMasculino_${asientoId}">Masculino</label>
                <input type="radio" class="form-check-input" name="sexo-${asientoId}" id="sexoFemenino_${asientoId}" value="F" required> 
                <label for="sexoFemenino_${asientoId}">Femenino</label>
            </div>
            <input class="form-control mb-2" id="correo_${asientoId}" placeholder="Correo electrónico" type="email" required>
            <div class="form-check">
            <input class="hidden" type="checkbox" id="brazos_${asientoId}">
            <label class="hidden" for="brazos_${asientoId}">Con menor en brazos</label>
            </div>
            <div class="form-check mb-2">
            <input class="form-check-input" type="checkbox" id="esMenor_${asientoId}" disabled>
            <label class="form-check-label disabled" for="esMenor_${asientoId}">Es menor de edad</label>
            </div>
            <button class="btn btn-secondary w-100" disabled
                onclick='FormManager.enviarDatosPasajero("${asientoNombre}", ${asientoId}); 
                try {
                    const collapse = document.getElementById("collapse-${asientoId}-ida") || document.getElementById("collapse-${asientoId}-vuelta");
                    if (collapse) {
                        const bsCollapse = bootstrap.Collapse.getOrCreateInstance(collapse);
                        bsCollapse.hide();
                    }
                } catch(e) {}
                '>
                Complete todos los campos
            </button>
        `;
    },

    enviarDatosPasajero(nombreAsiento, idAsiento) {
        if (!SeatManager.validarFormularioCompleto(idAsiento)) {
            toastr.error("Complete todos los campos obligatorios antes de guardar");
            return;
        }

        const datos = this.recopilarDatosFormulario(idAsiento);
        const venta = new Venta(...datos);

        Venta.guardarEnStorage(idAsiento, venta);
        toastr.success(`Datos del asiento ${nombreAsiento} guardados correctamente.`);
    },

    recopilarDatosFormulario(idAsiento) {
        const tipoDoc = document.getElementById(`tipo_doc_${idAsiento}`).value;
        const numDoc = document.getElementById(`numeroDocNuevo_${idAsiento}`).value;
        const nombres = document.getElementById(`nombres_${idAsiento}`).value;
        const apellidoPaterno = document.getElementById(`apellidoPaterno_${idAsiento}`).value;
        const apellidoMaterno = document.getElementById(`apellidoMaterno_${idAsiento}`).value;
        const fechaNacimiento = document.getElementById(`fechaNacimientoNuevo_${idAsiento}`).value;
        const telefono = document.getElementById(`telefono_${idAsiento}`).value;
        const correo = document.getElementById(`correo_${idAsiento}`).value;
        const brazos = document.getElementById(`brazos_${idAsiento}`).checked;
        const esMenor = document.getElementById(`esMenor_${idAsiento}`).checked;

        const recuperarSeleccion = document.querySelector(`input[name="sexo-${idAsiento}"]:checked`)?.id;
        const sexo = recuperarSeleccion?.includes("Masculino") ? 1 : 0;

        return [tipoDoc, numDoc, nombres, apellidoPaterno, apellidoMaterno, fechaNacimiento,
            telefono, recuperarSeleccion, sexo, correo, brazos, esMenor];
    }
};

// =============================================================================
// API RENIEC
// =============================================================================

const ReniecAPI = {
    debounceTimers: new Map(),

    initialize() {
        // Inicialización general
    },

    initializeForSeat(asiento) {
        const docInput = document.getElementById(`numeroDocNuevo_${asiento}`);
        const tipoDoc = document.getElementById(`tipo_doc_${asiento}`);
        const fechaNac = document.getElementById(`fechaNacimientoNuevo_${asiento}`);

        if (docInput) {
            docInput.addEventListener("input", () => {
                this.debounceSearch(asiento);
            });
        }

        if (tipoDoc) {
            tipoDoc.addEventListener("change", () => this.buscarPersona(asiento));
        }

        if (fechaNac) {
            fechaNac.addEventListener("change", () => this.validarEdad(asiento));
        }
    },

    debounceSearch(asiento) {
        if (this.debounceTimers.has(asiento)) {
            clearTimeout(this.debounceTimers.get(asiento));
        }

        const timer = setTimeout(() => this.buscarPersona(asiento), 1000);
        this.debounceTimers.set(asiento, timer);
    },

    async buscarPersona(asiento) {
        const tipoDocVal = document.getElementById(`tipo_doc_${asiento}`).value;
        const numDoc = document.getElementById(`numeroDocNuevo_${asiento}`).value.trim();

        if (!this.validarDatosConsulta(tipoDocVal, numDoc)) return;

        try {
            const response = await fetch(
                `${CONFIG.RUTAS.API_PERSONA}?tipoDoc=${encodeURIComponent(tipoDocVal)}&numDoc=${encodeURIComponent(numDoc)}`
            );
            const json = await response.json();

            if (json.Status === "success") {
                this.llenarFormularioConDatos(asiento, json.data);
            } else {
                this.limpiarFormulario(asiento);
                toastr.error(json.Msj, "ERROR");
            }
        } catch (err) {
            toastr.error("Ocurrió un error: " + (err.message || err));
        }
    },

    validarDatosConsulta(tipoDocVal, numDoc) {
        if (!tipoDocVal) {
            toastr.warning("El tipo de documento es obligatorio", "MENSAJE DEL SISTEMA");
            return false;
        }

        if (!(numDoc.length === 8 || numDoc.length === 11)) {
            return false;
        }

        return true;
    },

    llenarFormularioConDatos(asiento, datos) {
        const campos = {
            nombres: datos.nombres || datos.nombre || "",
            apellidoPaterno: datos.apellidoPaterno || datos.ape_paterno || "",
            apellidoMaterno: datos.apellidoMaterno || datos.ape_materno || "",
            correo: datos.email || "",
            telefono: datos.telefono || ""
        };

        Object.entries(campos).forEach(([campo, valor]) => {
            const elemento = document.getElementById(`${campo}_${asiento}`);
            if (elemento) elemento.value = valor;
        });

        if (datos.f_nacimiento) {
            const fechaElement = document.getElementById(`fechaNacimientoNuevo_${asiento}`);
            if (fechaElement) {
                fechaElement.value = moment(datos.f_nacimiento).format("YYYY-MM-DD");
                this.validarEdad(asiento);
            }
        }

        if (datos.sexo != null) {
            const masculino = document.getElementById(`sexoMasculino_${asiento}`);
            const femenino = document.getElementById(`sexoFemenino_${asiento}`);
            if (masculino && femenino) {
                masculino.checked = datos.sexo === 1;
                femenino.checked = datos.sexo !== 1;
            }
        }

        SeatManager.validarFormularioCompleto(asiento);
    },

    limpiarFormulario(asiento) {
        const campos = ['nombres', 'apellidoPaterno', 'apellidoMaterno'];
        const valoresDefault = ['Nombres', 'Apellido paterno', 'Apellido materno'];

        campos.forEach((campo, index) => {
            const elemento = document.getElementById(`${campo}_${asiento}`);
            if (elemento) elemento.value = valoresDefault[index];
        });
    },

    validarEdad(asiento) {
        const fechaNacimiento = document.getElementById(`fechaNacimientoNuevo_${asiento}`).value;
        if (!fechaNacimiento) return;

        const fechaActual = new Date();
        const fechaNac = new Date(fechaNacimiento);
        let edad = fechaActual.getFullYear() - fechaNac.getFullYear();
        const mes = fechaActual.getMonth() - fechaNac.getMonth();

        if (mes < 0 || (mes === 0 && fechaActual.getDate() < fechaNac.getDate())) {
            edad--;
        }

        const esMenorCheckbox = document.getElementById(`esMenor_${asiento}`);
        if (esMenorCheckbox) {
            esMenorCheckbox.checked = edad < 18;
        }

        if (edad < 18) {
            toastr.warning(
                "Menores a 18 años necesitan presentar autorización de sus padres o tutores para viajar",
                "MENSAJE DEL SISTEMA"
            );
        }
    }
};

// =============================================================================
// GESTIÓN DE TEMPORIZADOR
// =============================================================================

const TimerManager = {
    intervals: new Map(),

    iniciar(segundos, sufijo) {
        if (this.intervals.has(sufijo)) {
            clearInterval(this.intervals.get(sufijo));
        }

        const elemento = document.getElementById(`temporizador_${sufijo}`);
        if (!elemento) return;

        let tiempoRestante = segundos;

        const intervalo = setInterval(() => {
            const minutos = Math.floor(tiempoRestante / 60);
            const segundosRestantes = tiempoRestante % 60;
            const formatoTiempo = `${minutos.toString().padStart(2, '0')}:${segundosRestantes.toString().padStart(2, '0')}`;

            elemento.textContent = `Tiempo restante: ${formatoTiempo}`;
            tiempoRestante--;

            if (tiempoRestante < 0) {
                this.finalizar(sufijo);
            }
        }, 1000);

        this.intervals.set(sufijo, intervalo);
    },

    async finalizar(sufijo) {
        const intervalo = this.intervals.get(sufijo);
        if (intervalo) {
            clearInterval(intervalo);
            this.intervals.delete(sufijo);
        }

        const elemento = document.getElementById(`temporizador_${sufijo}`);
        if (elemento) {
            elemento.textContent = "¡Tiempo agotado!";
        }

        try {
            await SeatManager.liberarTodosLosAsientos();
            sessionStorage.removeItem('ventas');
            toastr.error('Tiempo agotado. Los asientos han sido liberados automáticamente.', 'TIEMPO AGOTADO');

            setTimeout(() => {
                App.resetearSistemaCompleto();
                NavigationManager.updateFormVisibility();
                toastr.info('Sistema reiniciado. Puede realizar una nueva búsqueda.');
            }, 3000);

        } catch (error) {
            toastr.warning('Tiempo agotado. Algunos asientos podrían no haberse liberado correctamente.');
        }
    },

    detener(sufijo) {
        const intervalo = this.intervals.get(sufijo);
        if (intervalo) {
            clearInterval(intervalo);
            this.intervals.delete(sufijo);
        }
    },

    detenerTodos() {
        this.intervals.forEach((intervalo, sufijo) => {
            clearInterval(intervalo);
        });
        this.intervals.clear();
    }
};

// =============================================================================
// GESTOR DE RECARGA/CIERRE DE PÁGINA
// =============================================================================

const PageUnloadManager = {
    init() {
        window.addEventListener('beforeunload', (event) => {
            this.handlePageUnload(event);
        });

        window.addEventListener('unload', () => {
            this.cleanupOnExit();
        });
    },

    handlePageUnload(event) {
        const hayProgreso = this.verificarProgreso();

        if (hayProgreso) {
            event.preventDefault();
            event.returnValue = '¿Estás seguro de que quieres salir? Perderás tu progreso de reserva.';
            this.cleanupOnExit();
            return '¿Estás seguro de que quieres salir? Perderás tu progreso de reserva.';
        }
    },

    verificarProgreso() {
        const hayAsientosSeleccionados = SeatManager?.asientosSeleccionados?.size > 0;
        const ventasStorage = sessionStorage.getItem('ventas');
        const hayVentas = ventasStorage && Object.keys(JSON.parse(ventasStorage)).length > 0;

        return hayAsientosSeleccionados || hayVentas;
    },

    cleanupOnExit() {
        try {
            const hayAsientosSeleccionados = SeatManager?.asientosSeleccionados?.size > 0;
            const ventasStorage = sessionStorage.getItem('ventas');
            const hayVentas = ventasStorage && Object.keys(JSON.parse(ventasStorage)).length > 0;

            if (hayAsientosSeleccionados || hayVentas) {
                const asientosParaLiberar = new Set();

                if (hayAsientosSeleccionados) {
                    SeatManager.asientosSeleccionados.forEach(id => asientosParaLiberar.add(id));
                }

                if (hayVentas) {
                    const ventas = JSON.parse(ventasStorage);
                    Object.keys(ventas).forEach(id => asientosParaLiberar.add(id));
                }

                const asientosArray = Array.from(asientosParaLiberar);
                asientosArray.forEach(asientoId => {
                    SeatManager.marcarAsientoComoDisponible(asientoId);
                });
            }

            sessionStorage.removeItem('ventas');
        } catch (error) {
            // Error manejado silenciosamente
        }
    }
};

// =============================================================================
// GESTIÓN DE PAGO (PARTE 1)
// =============================================================================

const PaymentManager = {
    metodosPagoBD: null,
    datosContacto: {},

    async initialize() {
        const selector = document.getElementById("selector_metodo_pago");
        if (!selector) return;

        try {
            this.metodosPagoBD = await this.obtenerMetodosPagoDesdeAPI();
            this.poblarTiposPago();
            this.configurarEventos();
            this.generarFormularioContactoDinamico();
        } catch (error) {
            toastr.error('Error al cargar métodos de pago');
        }
    },

    async obtenerMetodosPagoDesdeAPI() {
        try {
            const response = await fetch(CONFIG.RUTAS.METODOS, {
                method: 'GET',
                headers: { 'Content-Type': 'application/json' }
            });
            const data = await response.json();

            if (data.status == 1) {
                return data.data;
            } else {
                toastr.warning("Error al cargar los métodos");
                return {};
            }
        } catch (err) {
            toastr.error("Error al cargar los métodos de pago: " + (err.message || err));
            return {};
        }
    },

    generarFormularioContactoDinamico() {
        const accordionBody = document.querySelector('#collapseContacto .accordion-body');
        if (!accordionBody) return;

        accordionBody.innerHTML = `
            <div class="row g-3">
                <div class="col-md-12">
                    <label for="tipo_comprobante" class="form-label">Tipo de comprobante</label>
                    <select id="tipo_comprobante" class="form-select">
                        <option value=1>Boleta</option>
                        <option value=2>Factura</option>
                    </select>
                </div>
                
                <div id="datos_comprobante_dinamico" class="col-12">
                    <!-- Se llena dinámicamente -->
                </div>
            </div>
            
            <div class="mt-4 d-flex justify-content-end">
                <button id="btn_validar_contacto" class="btn btn-primary">
                    Siguiente <i class="fas fa-arrow-right"></i>
                </button>
            </div>
        `;

        this.renderizarCamposComprobante('1');
        this.configurarEventosComprobante();
    },

    configurarEventosComprobante() {
        const selectorComprobante = document.getElementById('tipo_comprobante');
        if (selectorComprobante) {
            selectorComprobante.addEventListener('change', (e) => {
                this.renderizarCamposComprobante(e.target.value);
            });
        }

        const btnValidar = document.getElementById('btn_validar_contacto');
        if (btnValidar) {
            btnValidar.addEventListener('click', () => {
                this.validarYProcederPago();
            });
        }
    },

    renderizarCamposComprobante(tipoComprobante) {
        const contenedor = document.getElementById('datos_comprobante_dinamico');
        if (!contenedor) return;

        if (tipoComprobante == '1') {
            contenedor.innerHTML = `
                <div class="row g-3">
                    <div class="col-md-6">
                        <label for="tipo_documento_contacto" class="form-label">Tipo de documento *</label>
                        <select id="tipo_documento_contacto" class="form-select">
                            <option value="DNI">DNI</option>
                            <option value="CE">Carné de Extranjería</option>
                        </select>
                    </div>
                    <div class="col-md-6">
                        <label for="numero_documento_contacto" class="form-label">Número de documento *</label>
                        <input type="text" id="numero_documento_contacto" class="form-control" minlength="8" maxlength="12" required>
                    </div>
                    <div class="col-md-12">
                        <label for="email_contacto" class="form-label">Correo electrónico *</label>
                        <input type="email" id="email_contacto" class="form-control" required>
                    </div>
                    <div class="col-md-12">
                        <label for="nombres_contacto" class="form-label">Nombres *</label>
                        <input type="text" id="nombres_contacto" class="form-control" required>
                    </div>
                    <div class="col-md-6">
                        <label for="apellido_paterno_contacto" class="form-label">Apellido Paterno *</label>
                        <input type="text" id="apellido_paterno_contacto" class="form-control" required>
                    </div>
                    <div class="col-md-6">
                        <label for="apellido_materno_contacto" class="form-label">Apellido Materno *</label>
                        <input type="text" id="apellido_materno_contacto" class="form-control" required>
                    </div>
                    <div class="col-md-12">
                        <label for="telefono_contacto" class="form-label">Teléfono/móvil *</label>
                        <input type="tel" id="telefono_contacto" class="form-control" required>
                    </div>
                </div>
            `;
        } else if (tipoComprobante == '2') {
            contenedor.innerHTML = `
                <div class="row g-3">
                    <div class="col-md-12">
                        <label for="email_contacto" class="form-label">Correo electrónico *</label>
                        <input type="email" id="email_contacto" class="form-control" required>
                    </div>
                    <div class="col-md-12">
                        <label for="numero_documento_contacto" class="form-label">RUC *</label>
                        <input type="text" id="numero_documento_contacto" class="form-control" placeholder="20123456789" maxlength="11" required>
                    </div>
                    <div class="col-md-12">
                        <label for="razon_social_contacto" class="form-label">Razón Social *</label>
                        <input type="text" id="razon_social_contacto" class="form-control" required>
                    </div>
                    <div class="col-md-12">
                        <label for="direccion_contacto" class="form-label">Dirección *</label>
                        <input type="text" id="direccion_contacto" class="form-control" required>
                    </div>
                    <div class="col-md-12">
                        <label for="telefono_contacto" class="form-label">Teléfono *</label>
                        <input type="tel" id="telefono_contacto" class="form-control" required>
                    </div>
                </div>
            `;
        }

        this.configurarValidacionCamposContacto();
        this.configurarConsultaAutomatica();
    },

    configurarValidacionCamposContacto() {
        const campos = ['email_contacto', 'numero_documento_contacto', 'nombres_contacto',
            'apellido_paterno_contacto', 'apellido_materno_contacto',
            'telefono_contacto', 'razon_social_contacto', 'direccion_contacto'];

        campos.forEach(campo => {
            const elemento = document.getElementById(campo);
            if (elemento) {
                elemento.addEventListener('blur', () => this.validarCampoContacto(campo));
                elemento.addEventListener('input', () => this.limpiarErrorCampo(campo));
            }
        });
    },

    configurarConsultaAutomatica() {
        let debounceTimer;
        const docInput = document.getElementById("numero_documento_contacto");
        const tipoComprobante = document.getElementById("tipo_comprobante").value;

        if (docInput) {
            docInput.addEventListener("input", () => {
                clearTimeout(debounceTimer);
                debounceTimer = setTimeout(() => this.consultarDocumentoContacto(tipoComprobante), 1000);
            });
        }
    },

    async consultarDocumentoContacto(tipoComprobante) {
        const numeroDoc = document.getElementById("numero_documento_contacto").value.trim();

        if (tipoComprobante === '1') {
            const tipoDoc = document.getElementById("tipo_documento_contacto").value;
            if ((tipoDoc === 'DNI' && numeroDoc.length === 8) ||
                (tipoDoc === 'CE' && numeroDoc.length >= 9 && numeroDoc.length <= 12)) {
                await this.consultarReniecContacto(tipoDoc, numeroDoc);
            }
        } else if (tipoComprobante == '2') {
            if (numeroDoc.length === 11) {
                await this.consultarSunatContacto("RUC", numeroDoc);
            }
        }
    },

    async consultarReniecContacto(tipoDoc, numeroDoc) {
        try {
            const response = await fetch(
                `${CONFIG.RUTAS.API_PERSONA}?tipoDoc=${encodeURIComponent(tipoDoc)}&numDoc=${encodeURIComponent(numeroDoc)}`
            );
            const json = await response.json();

            if (json.Status === "success") {
                const datos = json.data;

                const nombres = document.getElementById("nombres_contacto");
                const apellidoPaterno = document.getElementById("apellido_paterno_contacto");
                const apellidoMaterno = document.getElementById("apellido_materno_contacto");
                const telefono = document.getElementById("telefono_contacto");
                const email = document.getElementById("email_contacto");

                if (nombres) nombres.value = datos.nombres || datos.nombre || "";
                if (apellidoPaterno) apellidoPaterno.value = datos.apellidoPaterno || datos.ape_paterno || "";
                if (apellidoMaterno) apellidoMaterno.value = datos.apellidoMaterno || datos.ape_materno || "";
                if (telefono) telefono.value = datos.telefono || "";
                if (email) email.value = datos.email || "";

                toastr.success("Datos cargados automáticamente");
            }
        } catch (err) {
            // Error manejado silenciosamente
        }
    },

    async consultarSunatContacto(tipoDocVal, ruc) {
        try {
            const response = await fetch(
                `${CONFIG.RUTAS.API_SUNAT}?tipoDoc=${encodeURIComponent(tipoDocVal)}&numDoc=${encodeURIComponent(ruc)}`
            );
            const json = await response.json();

            if (json.Status === "success" || json.success) {
                const datos = json.data;

                const razonSocial = document.getElementById("razon_social_contacto");
                const direccion = document.getElementById("direccion_contacto");
                const telefono = document.getElementById("telefono_contacto");

                if (razonSocial) razonSocial.value = datos.razonSocial || datos.nombre_razon_social || "";
                if (direccion) direccion.value = datos.direccion || datos.direccion_completa || "";
                if (telefono) telefono.value = datos.telefono || "";

                toastr.success("Datos de la empresa cargados automáticamente");
            }
        } catch (err) {
            // Error manejado silenciosamente
        }
    },

    validarCampoContacto(campo) {
        const elemento = document.getElementById(campo);
        if (!elemento) return true;

        const valor = elemento.value.trim();
        const tipoComprobante = document.getElementById("tipo_comprobante").value;
        let esValido = true;
        let mensaje = "";

        switch (campo) {
            case 'email_contacto':
                esValido = /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(valor);
                mensaje = "Ingrese un correo electrónico válido";
                break;
            case 'numero_documento_contacto':
                if (tipoComprobante === '1') {
                    const tipoDoc = document.getElementById("tipo_documento_contacto").value;
                    if (tipoDoc === 'DNI') {
                        esValido = /^\d{8}$/.test(valor);
                        mensaje = "DNI debe tener 8 dígitos";
                    } else if (tipoDoc === 'CE') {
                        esValido = /^\d{9,12}$/.test(valor);
                        mensaje = "CE debe tener entre 9 y 12 dígitos";
                    }
                } else if (tipoComprobante == '2') {
                    esValido = /^\d{11}$/.test(valor);
                    mensaje = "RUC debe tener 11 dígitos";
                }
                break;
            case 'nombres_contacto':
            case 'apellido_paterno_contacto':
            case 'apellido_materno_contacto':
            case 'razon_social_contacto':
            case 'direccion_contacto':
                esValido = valor.length >= 2;
                mensaje = "Este campo debe tener al menos 2 caracteres";
                break;
            case 'telefono_contacto':
                esValido = /^\d{9}$/.test(valor);
                mensaje = "Teléfono debe tener 9 dígitos";
                break;
        }

        if (!esValido && valor) {
            this.mostrarErrorCampo(elemento, mensaje);
        } else {
            this.limpiarErrorCampo(campo);
        }

        return esValido;
    },

    validarYProcederPago() {
        if (!this.validarFormularioContactoCompleto()) {
            toastr.error("Por favor complete todos los campos requeridos correctamente");
            return;
        }

        if (!this.validarDatosPasajerosCompletos()) {
            toastr.error("Por favor complete los datos de todos los pasajeros");
            return;
        }

        const collapsePago = document.getElementById("collapsePago");
        if (collapsePago) {
            const bsCollapse = new bootstrap.Collapse(collapsePago, { show: true });
        }

        toastr.success("Datos de contacto validados correctamente");
    },

    validarFormularioContactoCompleto() {
        const tipoComprobante = document.getElementById("tipo_comprobante").value;
        let camposRequeridos = ['email_contacto', 'numero_documento_contacto', 'telefono_contacto'];

        if (tipoComprobante === '1') {
            camposRequeridos.push('nombres_contacto', 'apellido_paterno_contacto', 'apellido_materno_contacto');
        } else if (tipoComprobante == '2') {
            camposRequeridos.push('razon_social_contacto', 'direccion_contacto');
        }

        let todoValido = true;

        camposRequeridos.forEach(campo => {
            const elemento = document.getElementById(campo);
            if (!elemento || !elemento.value.trim()) {
                this.mostrarErrorCampo(elemento, 'Este campo es obligatorio');
                todoValido = false;
            } else if (!this.validarCampoContacto(campo)) {
                todoValido = false;
            }
        });

        return todoValido;
    },

    validarDatosPasajerosCompletos() {
        const ventas = JSON.parse(sessionStorage.getItem("ventas") || "{}");

        if (Object.keys(ventas).length === 0) {
            toastr.warning("No hay asientos seleccionados");
            return false;
        }

        const camposObligatorios = ['numDoc', 'nombres', 'apellidoPaterno', 'apellidoMaterno', 'telefono', 'correo'];

        for (const asientoId in ventas) {
            const venta = ventas[asientoId];

            for (const campo of camposObligatorios) {
                if (!venta[campo] || venta[campo].trim() === '') {
                    toastr.warning(`Complete los datos del pasajero en el asiento ${asientoId}`);
                    return false;
                }
            }
        }

        return true;
    },

    mostrarErrorCampo(elemento, mensaje) {
        if (!elemento) return;

        elemento.classList.add('is-invalid');

        const errorAnterior = elemento.parentNode.querySelector('.invalid-feedback');
        if (errorAnterior) errorAnterior.remove();

        const divError = document.createElement('div');
        divError.className = 'invalid-feedback';
        divError.textContent = mensaje;
        elemento.parentNode.appendChild(divError);
    },

    limpiarErrorCampo(campo) {
        const elemento = typeof campo === 'string' ? document.getElementById(campo) : campo;
        if (elemento) {
            elemento.classList.remove('is-invalid');
            const error = elemento.parentNode.querySelector('.invalid-feedback');
            if (error) error.remove();
        }
    },
    poblarTiposPago() {
        const selector = document.getElementById("selector_metodo_pago");
        if (!selector) return;

        selector.innerHTML = '<option value="">Seleccione</option>';

        for (const tipoId in this.metodosPagoBD) {
            const grupo = this.metodosPagoBD[tipoId];
            if (grupo.length > 0) {
                const tipoNombre = grupo[0].tipo_metodo;
                const option = document.createElement("option");
                option.value = tipoId;
                option.textContent = tipoNombre;
                selector.appendChild(option);
            }
        }
    },

    configurarEventos() {
        const selector = document.getElementById("selector_metodo_pago");
        if (!selector) return;

        selector.addEventListener("change", (e) => {
            this.mostrarMetodosPago(e.target.value);
        });
    },

    mostrarMetodosPago(tipoId) {
        const contenedor = document.getElementById("contenido_pago_dinamico");
        if (!contenedor) return;

        contenedor.innerHTML = "";

        if (!tipoId || !this.metodosPagoBD[tipoId]) return;

        const metodos = this.metodosPagoBD[tipoId];
        const tipoMetodo = metodos[0].tipo_metodo;

        const labelMetodo = document.createElement("label");
        labelMetodo.textContent = "Método de pago:";
        labelMetodo.className = "form-label";
        contenedor.appendChild(labelMetodo);

        const selectMetodo = document.createElement("select");
        selectMetodo.className = "form-select mb-3";
        selectMetodo.id = "metodo_pago_especifico";

        metodos.forEach((metodo) => {
            const option = document.createElement("option");
            option.value = metodo.id_metodo;
            option.textContent = metodo.metodo;
            option.dataset.qr = metodo.qr || '';
            option.dataset.logo = metodo.logo || '';
            selectMetodo.appendChild(option);
        });

        contenedor.appendChild(selectMetodo);

        this.renderizarContenidoMetodo(metodos[0], tipoMetodo);

        selectMetodo.addEventListener("change", (e) => {
            const metodoSeleccionado = metodos.find(m => m.id_metodo == e.target.value);
            if (metodoSeleccionado) {
                this.renderizarContenidoMetodo(metodoSeleccionado, tipoMetodo);
            }
        });

        this.agregarBotonFinalizarPago(contenedor);
    },

    renderizarContenidoMetodo(metodo, tipoMetodo) {
        const contenedor = document.getElementById("contenido_pago_dinamico");

        const existente = document.getElementById("extra_metodo_pago");
        if (existente) existente.remove();

        const divExtra = document.createElement("div");
        divExtra.id = "extra_metodo_pago";
        divExtra.className = "mb-3";

        if (tipoMetodo === "Tarjeta") {
            divExtra.innerHTML = `
                <div class="row g-3">
                    <div class="col-12">
                        <label class="form-label">Número de tarjeta</label>
                        <input id="numero_tarjeta" class="form-control" placeholder="1234 5678 9012 3456" maxlength="19">
                    </div>
                    <div class="col-12">
                        <label class="form-label">Nombre del titular</label>
                        <input id="titular_tarjeta" class="form-control" placeholder="Nombre completo como aparece en la tarjeta">
                    </div>
                    <div class="col-6">
                        <label class="form-label">Mes de vencimiento</label>
                        <select id="mes_vencimiento" class="form-select">
                            <option value="">MM</option>
                            ${Array.from({ length: 12 }, (_, i) => `<option value="${(i + 1).toString().padStart(2, '0')}">${(i + 1).toString().padStart(2, '0')}</option>`).join('')}
                        </select>
                    </div>
                    <div class="col-6">
                        <label class="form-label">Año de vencimiento</label>
                        <select id="ano_vencimiento" class="form-select">
                            <option value="">AA</option>
                            ${Array.from({ length: 10 }, (_, i) => {
                const year = new Date().getFullYear() + i;
                return `<option value="${year}">${year}</option>`;
            }).join('')}
                        </select>
                    </div>
                    <div class="col-6">
                        <label class="form-label">CVV</label>
                        <input id="cvv_tarjeta" class="form-control" placeholder="123" maxlength="4">
                    </div>
                    <div class="col-6">
                        <label class="form-label">Código promocional (opcional)</label>
                        <input id="codigo_promocional" class="form-control" placeholder="Ingrese código">
                    </div>
                </div>
            `;
        } else if (tipoMetodo === "BILLETERA VIRTUAL") {
            if (metodo.qr) {
                divExtra.innerHTML = `
                    <div class="text-center">
                        <p class="mb-3">Escanea el código QR con tu app de ${metodo.metodo}</p>
                        <img src="${metodo.qr}" alt="QR ${metodo.metodo}" style="max-width: 200px; border: 1px solid #ddd; border-radius: 8px;">
                        <p class="mt-3 text-muted small">Una vez realizado el pago, haz clic en "Finalizar Pago"</p>
                    </div>
                    <div class="mb-3">
                        <label class="form-label">Código promocional (opcional)</label>
                        <input id="codigo_promocional_billetera" class="form-control" placeholder="Ingrese código promocional">
                    </div>
                `;
            }
        } else if (tipoMetodo === "Efectivo") {
            divExtra.innerHTML = `
                <div class="alert alert-info">
                    <i class="fas fa-info-circle me-2"></i>
                    <strong>Instrucciones para pago en efectivo:</strong>
                    <ul class="mt-2 mb-0">
                        <li>Debe completar el pago en ventanilla dentro de las próximas 2 horas</li>
                        <li>Presente el código de reserva que se le asigne</li>
                        <li>El boleto será válido una vez confirmado el pago</li>
                    </ul>
                </div>
                <div class="mb-3">
                    <label class="form-label">Código promocional (opcional)</label>
                    <input id="codigo_promocional_efectivo" class="form-control" placeholder="Ingrese código promocional">
                </div>
            `;
        }

        const botonFinalizar = document.getElementById("btn_finalizar_pago");
        if (botonFinalizar) {
            contenedor.insertBefore(divExtra, botonFinalizar.parentElement);
        } else {
            contenedor.appendChild(divExtra);
        }
    },

    agregarBotonFinalizarPago(contenedor) {
        if (document.getElementById("btn_finalizar_pago")) return;

        const divBoton = document.createElement("div");
        divBoton.className = "d-grid gap-2 mt-4";
        divBoton.innerHTML = `
            <button id="btn_finalizar_pago" class="btn btn-success btn-lg">
                <i class="fas fa-credit-card me-2"></i>
                Finalizar Pago
            </button>
        `;

        contenedor.appendChild(divBoton);

        document.getElementById("btn_finalizar_pago").addEventListener("click", async () => {
            const tipoMetodo = document.getElementById("selector_metodo_pago").value;
            const metodoPago = document.getElementById("metodo_pago_especifico").value;

            let nombreTipoMetodo = await obtenerNombreTipoMetodo(tipoMetodo);
            let nombreMetodo = await obtenerNombreMetodo(metodoPago);

            if (nombreMetodo == "tarjeta de credito" || nombreMetodo == "tarjeta") {
                this.procesarPago();
            } else if (nombreTipoMetodo == "efectivo" && nombreMetodo == "efectivo") {
                this.procesarReserva();
            } else {
                toastr.info("Funcionalidad en desarrollo");
            }
        });
    },

    async procesarPago() {
        if (!this.validarFormularioCompleto()) {
            toastr.error("Por favor complete todos los campos requeridos");
            return;
        }

        const datosCompletos = this.capturarDatosPago();
        this.mostrarLoader();

        try {
            const response = await fetch(CONFIG.RUTAS.PROCESAR_PAGO, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(datosCompletos)
            });

            const resultado = await response.json();
            this.ocultarLoader();

            if (resultado.Status === 'success') {
                this.mostrarPagoExitoso(resultado);
            } else {
                throw new Error(resultado.Msj || 'Error en el procesamiento del pago');
            }

        } catch (error) {
            this.ocultarLoader();
            toastr.error("Error al procesar el pago: " + error.message);
        }
    },

    async procesarReserva() {
        if (!this.validarFormularioCompleto()) {
            toastr.error("Por favor complete todos los campos requeridos");
            return;
        }

        const datosCompletos = this.capturarDatosPago();
        this.mostrarLoader();

        try {
            const response = await fetch(CONFIG.RUTAS.PROCESAR_RESERVA, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(datosCompletos)
            });

            const resultado = await response.json();
            this.ocultarLoader();

            if (resultado.Status === 'success') {
                this.mostrarPagoExitoso(resultado);
            } else {
                throw new Error(resultado.Msj || 'Error en el procesamiento del pago');
            }

        } catch (error) {
            this.ocultarLoader();
            toastr.error("Error al procesar el pago: " + error.message);
        }
    },

    validarFormularioCompleto() {
        if (!this.validarFormularioContactoCompleto()) return false;

        const tipoMetodo = document.getElementById("selector_metodo_pago").value;
        if (!tipoMetodo) {
            toastr.warning("Debe seleccionar un método de pago");
            return false;
        }

        return this.validarCamposMetodoPago();
    },

    validarCamposMetodoPago() {
        const metodoEspecifico = document.getElementById("metodo_pago_especifico");
        if (!metodoEspecifico) return true;

        const metodoSeleccionado = metodoEspecifico.options[metodoEspecifico.selectedIndex].text;

        if (metodoSeleccionado.includes("Visa") || metodoSeleccionado.includes("Mastercard")) {
            const numeroTarjeta = document.getElementById("numero_tarjeta");
            const titularTarjeta = document.getElementById("titular_tarjeta");
            const mesVencimiento = document.getElementById("mes_vencimiento");
            const anoVencimiento = document.getElementById("ano_vencimiento");
            const cvv = document.getElementById("cvv_tarjeta");

            if (!numeroTarjeta?.value || !titularTarjeta?.value || !mesVencimiento?.value ||
                !anoVencimiento?.value || !cvv?.value) {
                toastr.warning("Complete todos los datos de la tarjeta");
                return false;
            }

            if (!/^\d{4}\s?\d{4}\s?\d{4}\s?\d{4}$/.test(numeroTarjeta.value.replace(/\s/g, ''))) {
                toastr.warning("Formato de número de tarjeta inválido");
                return false;
            }
        }

        return true;
    },

    capturarDatosPago() {
        const tipoComprobante = document.getElementById("tipo_comprobante").value;

        let datosContacto = {
            tipo_comprobante: tipoComprobante,
            email: document.getElementById("email_contacto").value.trim(),
            telefono: document.getElementById("telefono_contacto").value.trim()
        };

        if (tipoComprobante == '1') {
            datosContacto = {
                ...datosContacto,
                tipo_documento: document.getElementById("tipo_documento_contacto").value,
                numero_documento: document.getElementById("numero_documento_contacto").value.trim(),
                nombres: document.getElementById("nombres_contacto").value.trim(),
                apellido_paterno: document.getElementById("apellido_paterno_contacto").value.trim(),
                apellido_materno: document.getElementById("apellido_materno_contacto").value.trim()
            };
        } else if (tipoComprobante == '2') {
            datosContacto = {
                ...datosContacto,
                ruc: document.getElementById("numero_documento_contacto").value.trim(),
                razon_social: document.getElementById("razon_social_contacto").value.trim(),
                direccion: document.getElementById("direccion_contacto").value.trim()
            };
        }

        const tipoMetodo = document.getElementById("selector_metodo_pago").value;
        const metodoEspecifico = document.getElementById("metodo_pago_especifico")?.value;

        const datosPago = {
            tipo_metodo: tipoMetodo,
            metodo_especifico: metodoEspecifico,
            timestamp: new Date().toISOString()
        };

        if (document.getElementById("numero_tarjeta")) {
            datosPago.datos_especificos = {
                numero: document.getElementById("numero_tarjeta").value.replace(/\s/g, ''),
                titular: document.getElementById("titular_tarjeta").value,
                mes_vencimiento: document.getElementById("mes_vencimiento").value,
                ano_vencimiento: document.getElementById("ano_vencimiento").value,
                cvv: document.getElementById("cvv_tarjeta").value,
                codigo_promocional: document.getElementById("codigo_promocional")?.value || null
            };
        }

        if (document.getElementById("codigo_promocional_efectivo")) {
            datosPago.datos_especificos = {
                codigo_promocional: document.getElementById("codigo_promocional_efectivo").value || null,
                codigo_reserva: document.getElementById("codigo_reserva")?.textContent || null
            };
        }

        if (document.getElementById("codigo_promocional_billetera")) {
            datosPago.datos_especificos = {
                codigo_promocional: document.getElementById("codigo_promocional_billetera").value || null,
            };
        }

        return {
            contacto: datosContacto,
            pago: datosPago,
            ventas: JSON.parse(sessionStorage.getItem("ventas") || "{}"),
            itinerario: {
                currentStep: AppState.currentStep,
                itinerarioRegreso: AppState.itinerarioRegreso
            }
        };
    },

    generarCodigoReserva() {
        const timestamp = Date.now().toString(36);
        const random = Math.random().toString(36).substr(2, 5);
        return `RES-${timestamp}-${random}`.toUpperCase();
    },
    mostrarLoader() {
        const overlay = document.createElement('div');
        overlay.id = 'payment-loader-overlay';
        overlay.style.cssText = `
            position: fixed; top: 0; left: 0; width: 100%; height: 100%;
            background: rgba(0,0,0,0.7); display: flex; justify-content: center;
            align-items: center; z-index: 9999;
        `;

        overlay.innerHTML = `
            <div style="text-align: center; color: white;">
                <div class="spinner-border text-light" style="width: 4rem; height: 4rem;"></div>
                <h4 class="mt-3">Procesando pago...</h4>
                <p class="text-muted">Por favor espere mientras confirmamos su transacción</p>
            </div>
        `;

        document.body.appendChild(overlay);

        const boton = document.getElementById("btn_finalizar_pago");
        if (boton) {
            boton.disabled = true;
            boton.innerHTML = '<i class="fas fa-spinner fa-spin me-2"></i>Procesando...';
        }
    },

    ocultarLoader() {
        const overlay = document.getElementById('payment-loader-overlay');
        if (overlay) overlay.remove();

        const boton = document.getElementById("btn_finalizar_pago");
        if (boton) {
            boton.disabled = false;
            boton.innerHTML = '<i class="fas fa-credit-card me-2"></i>Finalizar Pago';
        }
    },

    mostrarPagoExitoso(resultado) {
        const overlay = document.createElement('div');
        overlay.id = 'payment-success-overlay';
        overlay.style.cssText = `
            position: fixed; top: 0; left: 0; width: 100%; height: 100%;
            background: linear-gradient(135deg, #d4f8d4 0%, #a8e6a8 100%);
            display: flex; justify-content: center; align-items: center; z-index: 9999;
            animation: fadeIn 0.5s ease-in;
        `;

        overlay.innerHTML = `
            <div style="text-align: center; animation: bounceIn 0.8s ease-out;">
                <div style="
                    width: 120px; height: 120px; border-radius: 50%; background: #28a745;
                    margin: 0 auto 30px; display: flex; align-items: center; justify-content: center;
                    animation: checkmarkAnimation 0.6s ease-in-out 0.3s both;
                ">
                    <i class="fas fa-check" style="color: white; font-size: 60px;"></i>
                </div>
                <h1 style="color: #155724; margin-bottom: 20px; font-weight: bold;">¡Pago Confirmado!</h1>
                <h4 style="color: #155724; margin-bottom: 15px;">Código de confirmación: <strong>${resultado.codigo_confirmacion || 'PAY-' + Date.now()}</strong></h4>
                <p style="color: #155724; font-size: 18px; margin-bottom: 30px;">
                    Su reserva ha sido procesada exitosamente.<br>
                    Recibirá un correo de confirmación en ${this.datosContacto.email || 'su email'}
                </p>
                <button id="btn_nueva_reserva" class="btn btn-success btn-lg" style="margin-right: 15px;">
                    <i class="fas fa-plus me-2"></i>Nueva Reserva
                </button>
                <button id="btn_descargar_boleto" class="btn btn-outline-success btn-lg">
                    <i class="fas fa-download me-2"></i>Descargar Boleto
                </button>
            </div>
        `;

        const style = document.createElement('style');
        style.textContent = `
            @keyframes fadeIn {
                from { opacity: 0; }
                to { opacity: 1; }
            }
            @keyframes bounceIn {
                0% { transform: scale(0.3); opacity: 0; }
                50% { transform: scale(1.05); opacity: 0.8; }
                70% { transform: scale(0.9); opacity: 0.9; }
                100% { transform: scale(1); opacity: 1; }
            }
            @keyframes checkmarkAnimation {
                0% { transform: scale(0); }
                50% { transform: scale(1.2); }
                100% { transform: scale(1); }
            }
        `;
        document.head.appendChild(style);

        document.body.appendChild(overlay);

        document.getElementById('btn_nueva_reserva').addEventListener('click', () => {
            this.iniciarNuevaReserva();
        });

        document.getElementById('btn_descargar_boleto').addEventListener('click', () => {
            this.descargarBoleto(resultado);
        });

        this.limpiarDatosReserva();
    },

    iniciarNuevaReserva() {
        const overlay = document.getElementById('payment-success-overlay');
        if (overlay) overlay.remove();

        App.resetearSistemaCompleto();
        NavigationManager.updateFormVisibility();
        window.scrollTo({ top: 0, behavior: 'smooth' });
        toastr.success('Listo para una nueva reserva');
    },

    descargarBoleto(resultado) {
        toastr.info('Preparando descarga del boleto...');

        setTimeout(() => {
            const link = document.createElement('a');
            link.href = '#';
            link.download = `boleto-${resultado.codigo_confirmacion || 'reserva'}.pdf`;
            link.click();
            toastr.success('Boleto descargado exitosamente');
        }, 1500);
    },

    limpiarDatosReserva() {
        sessionStorage.removeItem('ventas');
        sessionStorage.removeItem('datos_pago');
        this.datosContacto = {};
    },

    limpiarFormularioPago() {
        const tipoComprobante = document.getElementById("tipo_comprobante");
        if (tipoComprobante) {
            tipoComprobante.value = '1';
        }

        this.renderizarCamposComprobante('1');

        const selectorTipo = document.getElementById("selector_metodo_pago");
        if (selectorTipo) {
            selectorTipo.selectedIndex = 0;
        }

        const contenedorDinamico = document.getElementById("contenido_pago_dinamico");
        if (contenedorDinamico) {
            contenedorDinamico.innerHTML = '';
        }
    }
};

// =============================================================================
// APLICACIÓN PRINCIPAL
// =============================================================================

const App = {
    init() {
        this.configurarEventosGlobales();
        this.inicializarComponentes();
        NavigationManager.inicializarEstadoPorDefecto();
        PageUnloadManager.init();
        SetearConfig.init();
    },

    resetearSistemaCompletoSinRutas() {
        try {
            sessionStorage.removeItem('ventas');

            if (typeof SeatManager !== 'undefined') {
                SeatManager.asientosSeleccionados.clear();
            }

            const contenedorIda = document.getElementById('contenedor_viajes_ida');
            const contenedorVuelta = document.getElementById('contenedor_viajes_vuelta');

            if (contenedorIda) contenedorIda.innerHTML = '';
            if (contenedorVuelta) contenedorVuelta.innerHTML = '';

            AppState.currentStep = 0;
            AppState.maxStep = 0;
            AppState.itinerarioRegreso = null;

            document.querySelectorAll('[id^="accordionPasajeros_"]').forEach(accordion => {
                accordion.innerHTML = '';
            });

            document.querySelectorAll('[id^="contenido_datos_"]').forEach(contenedor => {
                contenedor.classList.add('d-none');
            });

        } catch (error) {
            // Error manejado silenciosamente
        }
    },

    resetearSistemaCompleto() {
        AppState.resetProgress();

        sessionStorage.removeItem('ventas');
        sessionStorage.removeItem('datos_pago');
        sessionStorage.clear();

        this.limpiarFormularios();
        this.limpiarContenedoresDinamicos();

        TimerManager.detenerTodos();
        this.limpiarAsientosSeleccionados();

        if (typeof PaymentManager !== 'undefined') {
            PaymentManager.limpiarFormularioPago();
        }

        if (typeof SeatManager !== 'undefined') {
            SeatManager.asientosSeleccionados.clear();
        }
    },

    limpiarFormularios() {
        $('#cbx_Ciudades').val(null).trigger('change');
        $('input[name="fecha_ida"]').val('');
        $('input[name="fecha_vuelta"]').val('');

        $('input[type="text"], input[type="email"], input[type="date"]').val('');
        $('input[type="checkbox"], input[type="radio"]').prop('checked', false);
        $('select').prop('selectedIndex', 0);
    },

    limpiarContenedoresDinamicos() {
        ['contenedor_viajes_ida', 'contenedor_viajes_vuelta'].forEach(id => {
            const contenedor = document.getElementById(id);
            if (contenedor) contenedor.innerHTML = '';
        });

        ['ida', 'vuelta'].forEach(sufijo => {
            const accordion = document.getElementById(`accordionPasajeros_${sufijo}`);
            if (accordion) accordion.innerHTML = '';

            const contenidoDatos = document.getElementById(`contenido_datos_${sufijo}`);
            if (contenidoDatos) contenidoDatos.classList.add('d-none');
        });

        ['ida', 'vuelta'].forEach(sufijo => {
            const contenedoresPiso2 = document.querySelectorAll(`[id^="contenedor_piso_2_"][id$="_${sufijo}"]`);
            contenedoresPiso2.forEach(el => {
                el.style.display = 'none';
                el.innerHTML = '';
            });
        });

        ['ida', 'vuelta'].forEach(sufijo => {
            const matrices = document.querySelectorAll(`[id^="matrizContainer_"][id$="_${sufijo}"]`);
            matrices.forEach(m => m.innerHTML = '');
        });
    },

    limpiarAsientosSeleccionados() {
        document.querySelectorAll('.asiento-seleccionado').forEach(asiento => {
            asiento.classList.remove('asiento-seleccionado');
            asiento.style.backgroundColor = '';
            asiento.style.color = '';
        });
    },

    configurarEventosGlobales() {
        $(document).on('click', '.btn-siguiente', () => {
            NavigationManager.goToNextStep();
        });

        // Hacer funciones globales accesibles
        window.buscarYMostrarItinerario = SearchManager.buscarYMostrarItinerario.bind(SearchManager);
        window.acabarPrimerItinerario = NavigationManager.confirmarDatosIda.bind(NavigationManager);
        window.acabarSegundoItinerario = NavigationManager.confirmarDatosRegreso.bind(NavigationManager);
        window.volverAItinerarioIda = NavigationManager.volverAItinerarioIda.bind(NavigationManager);
        window.enviarDatosPasajero = FormManager.enviarDatosPasajero.bind(FormManager);

        window.limpiarSistema = async () => {
            await this.resetearSistemaCompleto();
            NavigationManager.updateFormVisibility();
            toastr.success('Sistema limpiado correctamente');
        };
    },

    inicializarComponentes() {
        RouteManager.cargarRutas();
        NavigationManager.updateFormVisibility();
        NavigationManager.initializeTabEvents();
        RouteManager.formatearFechas();

        this.inicializarPagoCondicional();
    },

    inicializarPagoCondicional() {
        if (AppState.currentStep === 3) {
            PaymentManager.initialize();
        }

        const originalSetCurrentStep = AppState.setCurrentStep;
        AppState.setCurrentStep = function (step) {
            originalSetCurrentStep.call(this, step);
            if (step === 3) {
                setTimeout(() => {
                    PaymentManager.initialize();
                }, 100);
            }
        };
    }
};

// =============================================================================
// INICIALIZACIÓN AL CARGAR EL DOM
// =============================================================================

document.addEventListener('DOMContentLoaded', () => {
    App.init();
});