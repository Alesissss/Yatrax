// =============================================================================
// CONFIGURACIÓN Y CONSTANTES
// =============================================================================

const CONFIG = {
    MAX_ASIENTOS: 4, // Valor por defecto
    IGV: 0.18, // En decimal, en porcentaje 18%
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
    GRILLA: {
        FILAS: 15,
        COLUMNAS: 6
    }
};

const SetearConfig = {   
    init(){

    },

    setMaxAsientos(){

    }

}

async function obtenerNombreMetodo(idMetodo) {
    const response = await fetch(`/ecommerce/home/obtenerMetodoPagoxID/${idMetodo}`)
    const data = await response.text()
    return data;
}

async function obtenerNombreTipoMetodo(idTipo) {
    const response = await fetch(`/ecommerce/home/obtenerTipoMetodoxID/${idTipo}`)
    const data = await response.text()
    return data;
}

$.ajax({
    url: '/ecommerce/home/GetConfGeneral',  // Ruta de la API
    method: 'GET',  // Método GET
    success: function (data) {
        // Verificamos si la respuesta es exitosa
        if (data.Status === 'success' && data.data) {
            CONFIG.MAX_ASIENTOS = data.data.max_pasajes_venta;
            CONFIG.TIEMPO_MAXIMO_COMPRA = data.data.tiempo_maximo_venta_minutos;
            CONFIG.IGV = data.data.igv;
            console.log("MAX_ASIENTOS actualizado:", CONFIG.MAX_ASIENTOS);
        } else {
            console.error("Error al recuperar la configuración general");
        }
    },
    error: function (xhr, status, error) {
        console.error("Error en la llamada AJAX:", error);
    }
});



// =============================================================================
// ESTADO GLOBAL DE LA APLICACIÓN
// =============================================================================

const AppState = {
    currentStep: 0,
    maxStep: 0,
    itinerarioRegreso: null,

    // Getters y setters para controlar el estado
    setCurrentStep(step) {
        this.currentStep = step;
        if (step > this.maxStep) this.maxStep = step;
    },

    resetProgress() {
        this.currentStep = 0;
        this.maxStep = 0;
        this.itinerarioRegreso = null;
        console.log('🔄 Estado de la aplicación reseteado');
    }
};

// =============================================================================
// CLASE VENTA
// =============================================================================

class Venta {
    constructor(tipo_doc, numDoc, nombres, apellidoPaterno, apellidoMaterno, fechaNacimiento,
        telefono, seleccionSexo, sexo, correo, brazos, esMenor) {
        this.tipoDoc = tipo_doc
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
// GESTIÓN DE NAVEGACIÓN Y PESTAÑAS - VERSIÓN MEJORADA
// =============================================================================

const NavigationManager = {
    updateFormVisibility() {
        const form = document.getElementById('form-destino');
        const steps = document.querySelectorAll('.step');
        const tabs = document.querySelectorAll('.tab-link');

        // ✅ CORRECCIÓN: Solo ocultar formulario en tab 3 (pago)
        if (form) {
            form.classList.toggle('hidden', AppState.currentStep === 3);
        }

        // Actualizar pasos activos
        steps.forEach(step => step.classList.remove('active'));
        tabs.forEach(tab => tab.classList.remove('active', 'disabled'));

        if (steps[AppState.currentStep]) {
            steps[AppState.currentStep].classList.add('active');
        }
        if (tabs[AppState.currentStep]) {
            tabs[AppState.currentStep].classList.add('active');
        }

        // ✅ NUEVA LÓGICA: Control estricto de acceso a pestañas
        this.controlarAccesoTabs();
    },

    // ✅ NUEVA FUNCIÓN: Control estricto de acceso a tabs
    controlarAccesoTabs() {
        const tabs = document.querySelectorAll('.tab-link');

        tabs.forEach((tab, index) => {
            const stepIndex = parseInt(tab.getAttribute('data-step'));

            // Por defecto, deshabilitar todos los tabs
            tab.classList.add('disabled');
            tab.setAttribute('disabled', 'true');
            tab.style.pointerEvents = 'none';

            // Habilitar tabs según el estado actual
            if (this.puedeAccederATab(stepIndex)) {
                tab.classList.remove('disabled');
                tab.removeAttribute('disabled');
                tab.style.pointerEvents = 'auto';
            }
        });
    },

    // ✅ NUEVA FUNCIÓN: Determinar si se puede acceder a un tab específico
    puedeAccederATab(tabIndex) {
        switch (tabIndex) {
            case 0: // Tab "Elegir destino"
                // Solo se puede acceder si no hemos avanzado
                return AppState.currentStep === 0;

            case 1: // Tab "Itinerario ida"
                // Se puede acceder si estamos en él o si podemos volver desde tab 2
                return AppState.currentStep === 1 ||
                    (AppState.currentStep === 2 && this.tieneItinerarioRegreso());

            case 2: // Tab "Itinerario regreso"
                // Solo si estamos en él y hay itinerario de regreso
                return AppState.currentStep === 2 && this.tieneItinerarioRegreso();

            case 3: // Tab "Pago"
                // Solo si estamos en él
                return AppState.currentStep === 3;

            default:
                return false;
        }
    },

    // ✅ NUEVA FUNCIÓN: Verificar si hay itinerario de regreso
    tieneItinerarioRegreso() {
        const fechaVuelta = $("input[name='fecha_vuelta']").val();
        return fechaVuelta && fechaVuelta.trim() !== '' && AppState.itinerarioRegreso;
    },

    // ✅ FUNCIÓN MODIFICADA: Mostrar loader en cambios de tab
    async mostrarLoader(mensaje = "Cargando...") {
        const overlay = document.createElement('div');
        overlay.id = 'navigation-loader';
        overlay.style.cssText = `
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(0,0,0,0.7);
            display: flex;
            justify-content: center;
            align-items: center;
            z-index: 9999;
        `;

        overlay.innerHTML = `
            <div style="text-align: center; color: white;">
                <div class="spinner-border text-light" style="width: 3rem; height: 3rem;" role="status">
                    <span class="visually-hidden">Cargando...</span>
                </div>
                <h5 class="mt-3">${mensaje}</h5>
            </div>
        `;

        document.body.appendChild(overlay);

        // Simular carga mínima para mejor UX
        await new Promise(resolve => setTimeout(resolve, 800));
    },

    ocultarLoader() {
        const loader = document.getElementById('navigation-loader');
        if (loader) loader.remove();
    },

    // ✅ FUNCIÓN MODIFICADA: Ir al siguiente paso con loader
    async goToNextStep(mensaje = "Cargando...") {
        if (AppState.currentStep < 3) {
            await this.mostrarLoader(mensaje);
            AppState.setCurrentStep(AppState.currentStep + 1);
            this.updateFormVisibility();
            this.ocultarLoader();
        }
    },

    // ✅ FUNCIÓN MODIFICADA: Ir a paso específico con validaciones
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

    // ✅ NUEVA FUNCIÓN: Procesar búsqueda desde tab 0 a tab 1
    async procesarBusqueda() {
        await this.mostrarLoader("Buscando viajes disponibles...");

        // Avanzar a tab 1
        AppState.setCurrentStep(1);
        AppState.maxStep = Math.max(AppState.maxStep, 1);
        this.updateFormVisibility();

        this.ocultarLoader();
    },

    // ✅ NUEVA FUNCIÓN: Confirmar datos desde itinerario ida
    async confirmarDatosIda() {
        // Validar que se hayan completado todos los datos de pasajeros
        if (!this.validarDatosPasajerosCompletos()) {
            toastr.error("Por favor complete los datos de todos los pasajeros antes de continuar");
            return;
        }

        // Mostrar confirmación
        const confirmacion = await Swal.fire({
            title: '¿Todos los datos son correctos?',
            text: 'Verifica que toda la información de los pasajeros esté completa y sea correcta.',
            icon: 'question',
            showCancelButton: true,
            confirmButtonText: 'Sí, continuar',
            cancelButtonText: 'Revisar datos',
            confirmButtonColor: '#28a745',
            cancelButtonColor: '#6c757d'
        });

        if (!confirmacion.isConfirmed) return;

        // Verificar si hay fecha de vuelta
        const fechaVuelta = $("input[name='fecha_vuelta']").val();

        if (!fechaVuelta || fechaVuelta.trim() === '') {
            // No hay fecha de vuelta, ir directo al pago
            await this.irAPago();
            return;
        }

        // Verificar si hay itinerarios de regreso
        if (!AppState.itinerarioRegreso || AppState.itinerarioRegreso.length === 0) {
            toastr.warning("No existen itinerarios de regreso para la fecha seleccionada");
            await this.irAPago();
            return;
        }

        // Hay fecha de vuelta e itinerarios, ir a tab 2
        await this.irAItinerarioRegreso();
    },

    // ✅ NUEVA FUNCIÓN: Confirmar datos desde itinerario regreso
    async confirmarDatosRegreso() {
        // Validar que se hayan completado todos los datos de pasajeros
        if (!this.validarDatosPasajerosCompletos()) {
            toastr.error("Por favor complete los datos de todos los pasajeros antes de continuar");
            return;
        }

        // Mostrar confirmación
        const confirmacion = await Swal.fire({
            title: '¿Todos los datos son correctos?',
            text: 'Verifica que toda la información de los pasajeros esté completa y sea correcta.',
            icon: 'question',
            showCancelButton: true,
            confirmButtonText: 'Sí, ir al pago',
            cancelButtonText: 'Revisar datos',
            confirmButtonColor: '#28a745',
            cancelButtonColor: '#6c757d'
        });

        if (!confirmacion.isConfirmed) return;

        // Ir al pago
        await this.irAPago();
    },

    // ✅ NUEVA FUNCIÓN: Ir al itinerario de regreso
    async irAItinerarioRegreso() {
        await this.mostrarLoader("Cargando itinerario de regreso...");

        AppState.setCurrentStep(2);
        AppState.maxStep = Math.max(AppState.maxStep, 2);

        // Cargar itinerario de regreso
        setTimeout(() => {
            ItineraryManager.cargarItinerario(AppState.itinerarioRegreso, 'contenedor_viajes_vuelta', 'vuelta');
        }, 100);

        this.updateFormVisibility();
        this.ocultarLoader();
    },

    // ✅ NUEVA FUNCIÓN: Ir al pago
    async irAPago() {
        await this.mostrarLoader("Preparando información de pago...");

        AppState.setCurrentStep(3);
        AppState.maxStep = Math.max(AppState.maxStep, 3);

        // Inicializar sistema de pago
        setTimeout(() => {
            if (typeof PaymentManager !== 'undefined') {
                PaymentManager.initialize();
            }
        }, 100);

        this.updateFormVisibility();
        this.ocultarLoader();
    },

    // ✅ NUEVA FUNCIÓN: Validar datos de pasajeros completos
    validarDatosPasajerosCompletos() {
        const ventas = JSON.parse(sessionStorage.getItem("ventas") || "{}");

        if (Object.keys(ventas).length === 0) {
            toastr.warning("No hay asientos seleccionados");
            return false;
        }

        for (const asientoId in ventas) {
            const venta = ventas[asientoId];

            // Validar campos obligatorios
            const camposObligatorios = ['numDoc', 'nombres', 'apellidoPaterno', 'apellidoMaterno', 'telefono', 'correo'];

            for (const campo of camposObligatorios) {
                if (!venta[campo] || venta[campo].trim() === '') {
                    toastr.warning(`Complete los datos del pasajero en el asiento ${asientoId}`);
                    return false;
                }
            }
        }

        return true;
    },

    // ✅ NUEVA FUNCIÓN: Volver al itinerario de ida desde regreso
    async volverAItinerarioIda() {
        const confirmacion = await Swal.fire({
            title: '¿Volver al itinerario de ida?',
            text: 'Podrás modificar tu selección de asientos y datos de pasajeros.',
            icon: 'question',
            showCancelButton: true,
            confirmButtonText: 'Sí, volver',
            cancelButtonText: 'Cancelar',
            confirmButtonColor: '#17a2b8',
            cancelButtonColor: '#6c757d'
        });

        if (!confirmacion.isConfirmed) return;

        await this.goToStep(1, "Cargando itinerario de ida...");
    },

    initializeTabEvents() {
        document.querySelectorAll('.tab-link').forEach(tab => {
            tab.addEventListener('click', (event) => {
                const stepIndex = parseInt(tab.getAttribute('data-step'));

                // Prevenir comportamiento por defecto si no se puede acceder
                if (!this.puedeAccederATab(stepIndex)) {
                    event.preventDefault();
                    toastr.warning("No puedes acceder a esta sección en este momento.");
                    return;
                }

                this.goToStep(stepIndex);
            });
        });
    },

    // ✅ NUEVA FUNCIÓN: Inicializar estado por defecto
    inicializarEstadoPorDefecto() {
        AppState.currentStep = 0;
        AppState.maxStep = 0;
        AppState.itinerarioRegreso = null;
        this.updateFormVisibility();
        console.log('📍 Estado inicial: Tab 0 activo, otros deshabilitados');
    }
};
// =============================================================================
// GESTIÓN DE BÚSQUEDA Y DATOS - VERSIÓN MEJORADA
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

    // ✅ FUNCIÓN MODIFICADA: Búsqueda con validación de progreso
    async buscarYMostrarItinerario() {
        if (!this.validarDatos()) return;

        // ✅ NUEVO: Verificar si hay progreso y confirmar
        const hayProgreso = this.verificarProgreso();

        if (hayProgreso) {
            const confirmacion = await Swal.fire({
                title: "¿Realizar nueva búsqueda?",
                text: "Esta acción eliminará tu progreso actual, ¿estás seguro de hacerlo?",
                icon: "warning",
                showCancelButton: true,
                reverseButtons: true,
                confirmButtonText: "Sí, buscar",
                cancelButtonText: "Cancelar",
                confirmButtonColor: '#d33',
                cancelButtonColor: '#6c757d'
            });

            if (!confirmacion.isConfirmed) return;

            // Limpiar progreso antes de nueva búsqueda
            console.log('🔍 Progreso detectado - Iniciando limpieza automática...');
            await this.limpiarDatosPreviosCompleto();
        }

        // Ejecutar búsqueda
        await this.ejecutarBusqueda();
    },

    // ✅ NUEVA FUNCIÓN: Verificar si hay progreso actual (CRITERIO CORREGIDO)
    verificarProgreso() {
        // 1. Verificar asientos seleccionados en memoria (PRINCIPAL)
        const hayAsientosSeleccionados = SeatManager && SeatManager.asientosSeleccionados && SeatManager.asientosSeleccionados.size > 0;

        // 2. Verificar sessionStorage (datos confirmados)
        const ventasStorage = sessionStorage.getItem('ventas');
        const hayVentas = ventasStorage && Object.keys(JSON.parse(ventasStorage)).length > 0;

        console.log(`📊 Verificación de progreso:`, {
            asientosSeleccionados: hayAsientosSeleccionados,
            cantidadAsientos: SeatManager?.asientosSeleccionados?.size || 0,
            ventasStorage: !!hayVentas
        });

        // ✅ CRITERIO CORRECTO: Asientos seleccionados O datos en sessionStorage
        return hayAsientosSeleccionados || hayVentas;
    },

    // ✅ FUNCIÓN EXISTENTE: Limpieza automática completa
    async limpiarDatosPreviosCompleto() {
        console.log('🧹 Iniciando limpieza automática completa...');

        try {
            // 1. Liberar asientos en backend (TODOS los que estén seleccionados)
            if (SeatManager.asientosSeleccionados.size > 0) {
                console.log(`🔓 Liberando ${SeatManager.asientosSeleccionados.size} asientos en backend...`);
                await SeatManager.liberarTodosLosAsientos();
            }

            // 2. También liberar asientos desde sessionStorage por si quedaron huérfanos
            await this.liberarAsientosDesdeStorage();

            // 3. Resetear sistema completo (frontend)
            App.resetearSistemaCompleto();

            console.log('✅ Limpieza automática completada');

        } catch (error) {
            console.error('❌ Error en limpieza automática:', error);
            // Continuar con la búsqueda aunque haya error en limpieza
            App.resetearSistemaCompleto();
        }
    },

    // ✅ FUNCIÓN EXISTENTE: Liberar asientos desde sessionStorage
    async liberarAsientosDesdeStorage() {
        const ventasStorage = sessionStorage.getItem('ventas');
        if (!ventasStorage) return;

        try {
            const ventas = JSON.parse(ventasStorage);
            const asientosEnStorage = Object.keys(ventas);

            if (asientosEnStorage.length > 0) {
                console.log(`🔓 Liberando ${asientosEnStorage.length} asientos desde storage...`);

                const promesasLiberacion = asientosEnStorage.map(asientoId =>
                    SeatManager.marcarAsientoComoDisponible(asientoId)
                );

                await Promise.allSettled(promesasLiberacion);
                console.log('✅ Asientos del storage liberados');
            }
        } catch (error) {
            console.error('❌ Error liberando asientos desde storage:', error);
        }
    },

    // ✅ FUNCIÓN MODIFICADA: Ejecutar búsqueda con navegación mejorada
    async ejecutarBusqueda() {
        const datos = this.capturarDatos();

        // ✅ CORRECCIÓN: Resetear sistema SIN limpiar el combo de rutas
        App.resetearSistemaCompletoSinRutas();

        // ✅ CORRECCIÓN: Convertir jQuery AJAX a Promise para mejor control
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
                    console.error('Error en búsqueda:', error);
                    toastr.error("Error en la conexión al servidor.");
                    reject(error);
                }
            });
        });
    },

    // ✅ FUNCIÓN MODIFICADA: Procesar respuesta con navegación
    async procesarRespuestaBusqueda(resp) {
        if (resp.Status !== 'success') {
            toastr.warning('ERROR AL BUSCAR EL VIAJE: ' + resp.Msj);
            return;
        }

        if (!resp.data_ida || resp.data_ida.length === 0) {
            toastr.warning("No se han encontrado viajes para esas fechas");
            return;
        }

        // Cargar itinerario de ida
        ItineraryManager.cargarItinerario(resp.data_ida, 'contenedor_viajes_ida', 'ida');

        // Guardar itinerario de regreso si existe
        if (resp.data_vuelta) {
            AppState.itinerarioRegreso = resp.data_vuelta;
        } else {
            AppState.itinerarioRegreso = null;
        }

        // ✅ NUEVO: Usar NavigationManager para cambiar a tab 1
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
        });
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
// GESTIÓN DE ITINERARIOS - VERSIÓN CORREGIDA
// =============================================================================

const ItineraryManager = {
    async cargarItinerario(itinerarios, contenedorId, sufijo) {
        const contenedor = document.getElementById(contenedorId);
        contenedor.innerHTML = '';

        try {
            const response = await fetch(CONFIG.RUTAS.RENDERIZAR_ITINERARIO, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ itinerarios, sufijo })
            });

            const data = await response.json();
            contenedor.innerHTML = data.html;

            // ✅ CORRECCIÓN: Usar timeout más largo para asegurar que el DOM esté listo
            setTimeout(() => {
                this.inicializarEventosPostRender(sufijo);
            }, 200);

        } catch (err) {
            toastr.error("Error al renderizar el itinerario: " + (err.message || err));
        }
    },

    inicializarEventosPostRender(sufijo) {
        console.log(`🚀 Inicializando eventos post-render para: ${sufijo}`);

        ReniecAPI.initialize();
        this.configurarFuncionalidadElegir(sufijo);

        // ✅ CORRECCIÓN: Verificar que los elementos existan antes de configurar
        const botones = document.querySelectorAll(`.mostrarContenido_${sufijo}`);
        console.log(`📊 Encontrados ${botones.length} botones para ${sufijo}`);
    },

    configurarFuncionalidadElegir(sufijo) {
        // ✅ CORRECCIÓN: Usar delegación de eventos más robusta
        document.addEventListener('click', (event) => {
            // Verificar si el elemento clickeado tiene la clase correcta
            if (event.target.classList.contains(`mostrarContenido_${sufijo}`)) {
                const btn = event.target;
                console.log(`🎯 Click detectado en botón: ${btn.id} para ${sufijo}`);

                // Prevenir ejecución múltiple
                event.stopPropagation();

                // Ejecutar generación de matrices
                VehicleLayoutManager.generarMatrices(btn.id, sufijo);
            }
        });

        // ✅ CORRECCIÓN: Configurar eventos de acordeón con mejor manejo
        document.querySelectorAll(`.mostrarContenido_${sufijo}`).forEach(btn => {
            const targetId = btn.getAttribute('data-bs-target');
            const target = document.querySelector(targetId);

            if (target) {
                // ✅ NUEVO: Manejar evento shown.bs.collapse correctamente
                target.addEventListener('shown.bs.collapse', () => {
                    console.log(`📂 Acordeón abierto para ${sufijo}`);

                    // Pequeño delay para asegurar que el contenido esté renderizado
                    setTimeout(() => {
                        SeatManager.inicializarSeleccionAsientos(sufijo);
                        TimerManager.iniciar(300, sufijo);

                        // ✅ CORRECCIÓN: Restaurar estado si hay asientos seleccionados
                        VehicleLayoutManager.restaurarEstadoAsientos(sufijo);
                    }, 150);
                });

                // ✅ NUEVO: Manejar evento hidden.bs.collapse
                target.addEventListener('hidden.bs.collapse', () => {
                    console.log(`📁 Acordeón cerrado para ${sufijo}`);
                    // Detener timer cuando se cierre el acordeón
                    TimerManager.detener(sufijo);
                });
            }
        });

        console.log(`✅ Funcionalidad de elegir configurada para ${sufijo}`);
    },

    finalizarPrimerItinerario() {
        // Validar que todos los pasajeros tengan datos completos
        if (!this.validarDatosPasajerosCompletos()) {
            toastr.error("Por favor complete los datos de todos los pasajeros antes de continuar");
            return;
        }

        if (!AppState.itinerarioRegreso || AppState.itinerarioRegreso.length === 0) {
            AppState.setCurrentStep(3);
            setTimeout(() => PaymentManager.initialize(), 100);
        } else {
            AppState.setCurrentStep(2);

            // ✅ CORRECCIÓN: Usar timeout más largo para vuelta
            setTimeout(() => {
                this.cargarItinerario(AppState.itinerarioRegreso, 'contenedor_viajes_vuelta', 'vuelta');
            }, 300);
        }
        NavigationManager.updateFormVisibility();
    },

    validarDatosPasajerosCompletos() {
        const ventas = JSON.parse(sessionStorage.getItem("ventas") || "{}");

        if (Object.keys(ventas).length === 0) {
            toastr.warning("No hay asientos seleccionados");
            return false;
        }

        for (const asientoId in ventas) {
            const venta = ventas[asientoId];

            // Validar campos obligatorios (excepto checkboxes)
            const camposObligatorios = ['numDoc', 'nombres', 'apellidoPaterno', 'apellidoMaterno', 'telefono', 'correo'];

            for (const campo of camposObligatorios) {
                if (!venta[campo] || venta[campo].trim() === '') {
                    toastr.warning(`Complete los datos del pasajero en el asiento ${asientoId}`);
                    return false;
                }
            }
        }

        return true;
    }
};
// =============================================================================
// GESTIÓN DE DISEÑO DEL VEHÍCULO - VERSIÓN CORREGIDA
// =============================================================================

const VehicleLayoutManager = {
    async generarMatrices(idBoton, sufijo) {
        try {
            console.log(`🎨 Generando matrices para ${idBoton} - ${sufijo}`);

            const response = await fetch(CONFIG.RUTAS.OBTENER_DISENO_VEHICULO, {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ id_dv: idBoton })
            });

            const res = await response.json();
            const datos = res.data;

            const datosPiso1 = datos.filter(d => d.nroPiso == 1);
            const datosPiso2 = datos.filter(d => d.nroPiso == 2);

            // ✅ CORRECCIÓN: Regenerar matriz manteniendo asientos seleccionados
            this.generarMatrizDesdeDatos(datosPiso1, 1, `${idBoton}_${sufijo}`, sufijo);

            if (datosPiso2.length > 0) {
                document.getElementById(`contenedor_piso_2_${idBoton}_${sufijo}`).style.display = 'block';
                this.generarMatrizDesdeDatos(datosPiso2, 2, `${idBoton}_${sufijo}`, sufijo);
            } else {
                document.getElementById(`contenedor_piso_2_${idBoton}_${sufijo}`).style.display = 'none';
            }

            // ✅ CORRECCIÓN: Restaurar estado de asientos después de regenerar
            this.restaurarEstadoAsientos(sufijo);

        } catch (error) {
            console.error("Error detallado:", error);
            toastr.error("Error al cargar el diseño del vehículo");
        }
    },

    generarMatrizDesdeDatos(datos, piso, sufijo, tipoItinerario) {
        const contenedor = document.getElementById(`matrizContainer_${piso}_${sufijo}`);
        if (!contenedor) return;

        contenedor.innerHTML = '';
        this.configurarEstilosMatriz(contenedor);

        for (let y = 1; y <= CONFIG.GRILLA.FILAS; y++) {
            for (let x = 1; x <= CONFIG.GRILLA.COLUMNAS; x++) {
                // ✅ CORRECCIÓN: Pasar tipoItinerario para identificar correctamente
                const btn = this.crearElementoMatriz(datos, x, y, tipoItinerario);
                contenedor.appendChild(btn);
            }
        }
    },

    configurarEstilosMatriz(contenedor) {
        Object.assign(contenedor.style, {
            display: 'grid',
            gridTemplateColumns: `repeat(${CONFIG.GRILLA.COLUMNAS}, 40px)`,
            gridTemplateRows: `repeat(${CONFIG.GRILLA.FILAS}, 40px)`,
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
        Object.assign(btn.style, {
            width: '40px',
            height: '40px'
        });

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
            // ✅ CORRECCIÓN: Verificar si el asiento ya está en nuestro control local
            const estaSeleccionadoLocalmente = SeatManager.asientosSeleccionados.has(dato.id_asiento);

            if (estaSeleccionadoLocalmente) {
                // Asiento seleccionado por nosotros - verde
                btn.className = 'border border-dark border-2 asiento-seleccionado';
                btn.style.backgroundColor = '#28a745';
                btn.style.color = 'white';
                btn.innerText = dato.nombre;
                btn.style.cursor = 'pointer';
            } else if (dato.estado === 1) {
                // Asiento disponible - blanco con borde negro
                btn.className = 'border border-dark border-2 bg-white';
                btn.innerText = dato.nombre;
                btn.style.cursor = 'pointer';
            } else {
                // Asiento ocupado por otros - negro con texto blanco
                btn.className = 'border border-dark border-2 bg-dark text-white';
                btn.innerText = dato.nombre;
                btn.style.cursor = 'not-allowed';
                btn.disabled = true;
                btn.title = 'Asiento ocupado';
            }
        } else {
            // Otra herramienta
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

    // ✅ NUEVA FUNCIÓN: Restaurar estado visual de asientos seleccionados
    restaurarEstadoAsientos(sufijo) {
        console.log(`🔄 Restaurando estado de asientos para ${sufijo}`);

        // Restaurar estado visual de asientos seleccionados
        SeatManager.asientosSeleccionados.forEach(asientoId => {
            const btnAsiento = document.getElementById(asientoId);
            if (btnAsiento && btnAsiento.getAttribute('data-tipo') === '1') {
                btnAsiento.classList.add("asiento-seleccionado");
                btnAsiento.style.backgroundColor = '#28a745';
                btnAsiento.style.color = 'white';

                console.log(`✅ Asiento ${asientoId} restaurado como seleccionado`);
            }
        });

        // Reinicializar eventos de selección después de regenerar
        setTimeout(() => {
            SeatManager.inicializarSeleccionAsientos(sufijo);
        }, 100);
    }
};
// =============================================================================
// GESTIÓN DE ASIENTOS CON VALIDACIONES Y API (PARTE 1)
// =============================================================================

const SeatManager = {
    asientosSeleccionados: new Set(),
    // =============================================================================
    // GESTIÓN DE ASIENTOS - FUNCIÓN DE INICIALIZACIÓN MEJORADA
    // =============================================================================

    // ✅ CORRECCIÓN: Mejorar inicialización de selección de asientos
    inicializarSeleccionAsientos(sufijo) {
        console.log(`💺 Inicializando selección de asientos para: ${sufijo}`);

        // Remover listeners anteriores para evitar duplicados
        const asientosPrevios = document.querySelectorAll(`[data-tipo="1"][data-listener-${sufijo}="true"]`);
        asientosPrevios.forEach(btn => {
            btn.removeAttribute(`data-listener-${sufijo}`);
        });

        const asientos = document.querySelectorAll('[data-tipo="1"]');
        console.log(`📊 Encontrados ${asientos.length} asientos en total`);

        if (asientos.length === 0) {
            console.warn("No se encontraron asientos con data-tipo='1'");
            return;
        }

        let asientosConfigurados = 0;

        asientos.forEach(btn => {
            // ✅ CORRECCIÓN: Solo agregar listener si no está deshabilitado y no tiene listener previo
            const yaConfigurado = btn.getAttribute(`data-listener-${sufijo}`) === 'true';

            if (!btn.disabled && !yaConfigurado) {
                // Marcar como configurado para evitar duplicados
                btn.setAttribute(`data-listener-${sufijo}`, 'true');

                // Remover listeners anteriores
                const nuevoBtn = btn.cloneNode(true);
                btn.parentNode.replaceChild(nuevoBtn, btn);

                // Agregar nuevo listener
                nuevoBtn.addEventListener('click', (event) => {
                    console.log(`🎯 Click en asiento: ${event.target.id} (${sufijo})`);
                    this.manejarClickAsiento(event, sufijo);
                });

                asientosConfigurados++;
            }
        });

        console.log(`✅ ${asientosConfigurados} asientos configurados con listeners para ${sufijo}`);

        // ✅ CORRECCIÓN: Restaurar estado visual inmediatamente
        this.restaurarEstadoVisualAsientos(sufijo);
    },

    // ✅ NUEVA FUNCIÓN: Restaurar estado visual específicamente
    restaurarEstadoVisualAsientos(sufijo) {
        this.asientosSeleccionados.forEach(asientoId => {
            const btnAsiento = document.getElementById(asientoId);
            if (btnAsiento && btnAsiento.getAttribute('data-tipo') === '1') {
                // Verificar que no esté ya marcado para evitar duplicados
                if (!btnAsiento.classList.contains("asiento-seleccionado")) {
                    btnAsiento.classList.add("asiento-seleccionado");
                    btnAsiento.style.backgroundColor = '#28a745';
                    btnAsiento.style.color = 'white';

                    console.log(`🔄 Estado visual restaurado para asiento: ${asientoId}`);
                }

                // Mostrar contenedor de datos si hay asientos seleccionados
                const contenedor = document.getElementById(`contenido_datos_${sufijo}`);
                if (contenedor && contenedor.classList.contains("d-none")) {
                    contenedor.classList.remove("d-none");
                }
            }
        });
    },
    // ✅ FUNCIÓN MEJORADA: Liberar todos los asientos con mejor logging
    async liberarTodosLosAsientos() {
        console.log('🔓 Liberando todos los asientos seleccionados...');

        const promesasLiberacion = [];
        const asientosParaLiberar = [...this.asientosSeleccionados]; // Crear copia del Set

        // Liberar desde el Set de asientos seleccionados
        for (const asientoId of asientosParaLiberar) {
            promesasLiberacion.push(
                this.marcarAsientoComoDisponible(asientoId)
                    .then(resultado => ({ asientoId, resultado, origen: 'memoria' }))
                    .catch(error => ({ asientoId, error, origen: 'memoria' }))
            );
        }

        // También liberar asientos desde sessionStorage por si hay inconsistencias
        const ventas = JSON.parse(sessionStorage.getItem("ventas") || "{}");
        for (const asientoId in ventas) {
            if (!this.asientosSeleccionados.has(asientoId)) {
                promesasLiberacion.push(
                    this.marcarAsientoComoDisponible(asientoId)
                        .then(resultado => ({ asientoId, resultado, origen: 'storage' }))
                        .catch(error => ({ asientoId, error, origen: 'storage' }))
                );
            }
        }

        // Ejecutar todas las liberaciones en paralelo
        if (promesasLiberacion.length > 0) {
            try {
                const resultados = await Promise.allSettled(promesasLiberacion);

                let exitosos = 0;
                let fallidos = 0;

                resultados.forEach((resultado, index) => {
                    if (resultado.status === 'fulfilled') {
                        const { asientoId, resultado: res, error, origen } = resultado.value;
                        if (error) {
                            console.warn(`⚠️ Error liberando asiento ${asientoId} (${origen}):`, error);
                            fallidos++;
                        } else {
                            console.log(`✅ Asiento ${asientoId} liberado exitosamente (${origen})`);
                            exitosos++;
                        }
                    } else {
                        console.error(`❌ Error en promesa de liberación:`, resultado.reason);
                        fallidos++;
                    }
                });

                console.log(`📊 Resultado: ${exitosos} exitosos, ${fallidos} fallidos de ${promesasLiberacion.length} total`);

            } catch (error) {
                console.error('❌ Error liberando algunos asientos:', error);
            }
        } else {
            console.log('ℹ️ No hay asientos para liberar');
        }

        // Limpiar el Set local independientemente del resultado de la API
        this.asientosSeleccionados.clear();
        console.log('🧹 Set de asientos seleccionados limpiado');
    },

    async manejarClickAsiento(event, sufijo) {
        const btn = event.target;
        const nombreAsiento = btn.innerText.trim();
        const asientoId = btn.id;
        const accordionItemId = `collapse-${btn.id}-${sufijo}`;

        // Verificar si ya está seleccionado
        if (btn.classList.contains("asiento-seleccionado")) {
            await this.deseleccionarAsiento(btn, nombreAsiento, accordionItemId, asientoId, sufijo);
            return;
        }

        // Verificar límite de asientos
        if (!this.puedeSeleccionarAsiento()) {
            toastr.warning(`Solo puedes seleccionar hasta ${CONFIG.MAX_ASIENTOS} asientos.`);
            return;
        }

        // Llamar API para marcar como ocupado
        const ocupadoExitoso = await this.marcarAsientoComoOcupado(asientoId);
        if (!ocupadoExitoso) {
            toastr.error("Error al reservar el asiento. Intente nuevamente.");
            return;
        }

        // Seleccionar asiento
        this.seleccionarAsiento(btn, nombreAsiento, accordionItemId, sufijo);
    },

    async marcarAsientoComoOcupado(asientoId) {
        try {
            const response = await fetch(CONFIG.RUTAS.MARCAR_ASIENTO_OCUPADO, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    asiento_id: asientoId
                })
            });

            const resultado = await response.json();

            if (resultado.status === 1) {
                console.log(`✅ Asiento ${asientoId} marcado como ocupado`);
                return true;
            } else {
                console.error('❌ Error al marcar asiento como ocupado:', resultado.message);
                return false;
            }
        } catch (error) {
            console.error('❌ Error en llamada API para ocupar asiento:', error);
            return false;
        }
    },

    async marcarAsientoComoDisponible(asientoId) {
        try {
            const response = await fetch(CONFIG.RUTAS.MARCAR_ASIENTO_DISPONIBLE, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    asiento_id: asientoId
                })
            });

            const resultado = await response.json();

            if (resultado.status === 1) {
                console.log(`✅ Asiento ${asientoId} marcado como disponible`);
                return true;
            } else {
                console.error('❌ Error al marcar asiento como disponible:', resultado.message);
                return false;
            }
        } catch (error) {
            console.error('❌ Error en llamada API para liberar asiento:', error);
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
        });

        if (confirm.isConfirmed) {
            // Llamar API para marcar como disponible
            const liberadoExitoso = await this.marcarAsientoComoDisponible(asientoId);
            if (!liberadoExitoso) {
                toastr.warning("Error al liberar el asiento, pero se procederá con la deselección");
            }

            // Remover de la lista de seleccionados
            this.asientosSeleccionados.delete(asientoId);

            btn.classList.remove("asiento-seleccionado");
            // 🔧 RESTAURAR ESTADO VISUAL ORIGINAL DEL ASIENTO
            btn.className = 'border border-dark border-2 bg-white'; // Restaurar clases originales
            btn.innerText = nombreAsiento; // Restaurar el nombre del asiento
            btn.style.backgroundColor = ''; // Limpiar estilos inline
            btn.style.color = ''; // Limpiar estilos inline
            btn.style.cursor = 'pointer'; // Restaurar cursor clickeable
            btn.disabled = false; // Asegurar que no esté deshabilitado

            const accordionItem = document.getElementById(accordionItemId)?.closest(".accordion-item");
            if (accordionItem) accordionItem.remove();

            // Eliminar del sessionStorage
            const ventas = JSON.parse(sessionStorage.getItem("ventas") || "{}");
            delete ventas[asientoId];
            sessionStorage.setItem("ventas", JSON.stringify(ventas));

            // Ocultar contenedor si no hay asientos seleccionados
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
        // Agregar a la lista de seleccionados
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
        nuevoForm.innerHTML = this.generarHTMLFormulario(
            headerId, accordionItemId, btn.id, nombreAsiento, isFirstAccordion, sufijo
        );

        accordion.appendChild(nuevoForm);
        ReniecAPI.initializeForSeat(btn.id);

        // Configurar validación en tiempo real para este formulario
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
                campo.addEventListener('input', () => this.validarFormularioCompleto(asientoId));
                campo.addEventListener('blur', () => this.validarCampoEnTiempoReal(campoId));
            }
        });

        // Validar radio buttons de sexo
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

        // Validaciones específicas
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
            const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            esValido = emailRegex.test(valor);
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

        // Mostrar/ocultar error
        if (!esValido && valor) {
            this.mostrarErrorCampo(campo, mensaje);
        } else {
            this.limpiarErrorCampo(campo);
        }
    },

    validarFormularioCompleto(asientoId) {
        const camposObligatorios = [
            `tipo_doc_${asientoId}`, `numeroDocNuevo_${asientoId}`, `nombres_${asientoId}`,
            `apellidoPaterno_${asientoId}`, `apellidoMaterno_${asientoId}`,
            `fechaNacimientoNuevo_${asientoId}`, `telefono_${asientoId}`, `correo_${asientoId}`
        ];

        let todosCompletos = true;

        // Verificar campos obligatorios
        for (const campoId of camposObligatorios) {
            const campo = document.getElementById(campoId);
            if (!campo || !campo.value.trim()) {
                todosCompletos = false;
                break;
            }
        }

        // Verificar selección de sexo
        const masculino = document.getElementById(`sexoMasculino_${asientoId}`);
        const femenino = document.getElementById(`sexoFemenino_${asientoId}`);

        if (!masculino?.checked && !femenino?.checked) {
            todosCompletos = false;
        }

        // Actualizar botón de guardar
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

    mostrarErrorCampo(elemento, mensaje) {
        elemento.classList.add('is-invalid');

        // Remover mensaje anterior si existe
        const errorAnterior = elemento.parentNode.querySelector('.invalid-feedback');
        if (errorAnterior) errorAnterior.remove();

        // Agregar nuevo mensaje
        const divError = document.createElement('div');
        divError.className = 'invalid-feedback';
        divError.textContent = mensaje;
        elemento.parentNode.appendChild(divError);
    },

    limpiarErrorCampo(elemento) {
        elemento.classList.remove('is-invalid');
        const error = elemento.parentNode.querySelector('.invalid-feedback');
        if (error) error.remove();
    },

    generarHTMLFormulario(headerId, accordionItemId, btnId, nombreAsiento, isFirstAccordion, sufijo) {
        return `
            <h2 class="accordion-header" id="${headerId}">
                <button class="accordion-button ${!isFirstAccordion ? 'collapsed' : ''}" 
                        type="button" data-bs-toggle="collapse" 
                        data-bs-target="#${accordionItemId}" 
                        aria-expanded="${isFirstAccordion}" 
                        aria-controls="${accordionItemId}">
                    Asiento ${btnId}   
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
            <div class="mb-2 fw-bold text-primary">Asiento: ${asientoNombre} (<span>S/0.00</span>)</div>
            <select class="form-select mb-2" id="tipo_doc_${asientoId}">
            <option value="DNI">DNI</option>
            <option value="CE">CE</option>
            </select>
            <input class="form-control mb-2" id="numeroDocNuevo_${asientoId}" placeholder="N° Documento">
            <input class="form-control mb-2" id="nombres_${asientoId}" placeholder="Nombres">
            <input class="form-control mb-2" id="apellidoPaterno_${asientoId}" placeholder="Apellido paterno">
            <input class="form-control mb-2" id="apellidoMaterno_${asientoId}" placeholder="Apellido materno">
            <input class="form-control mb-2" id="fechaNacimientoNuevo_${asientoId}" type="date" placeholder="Fecha nacimiento">
            <input class="form-control mb-2" id="telefono_${asientoId}" placeholder="Teléfono">
            <div class="mb-2">
            <label class="me-2">Sexo:</label>
            <input type="radio" class="form-check-input" name="sexo-${asientoId}" id="sexoMasculino_${asientoId}" value="M"> 
            <label for="sexoMasculino_${asientoId}">Masculino</label>
            <input type="radio" class="form-check-input" name="sexo-${asientoId}" id="sexoFemenino_${asientoId}" value="F"> 
            <label for="sexoFemenino_${asientoId}">Femenino</label>
            </div>
            <input class="form-control mb-2" id="correo_${asientoId}" placeholder="Correo electrónico" type="email">
            <div class="form-check">
            <input class="form-check-input" type="checkbox" id="brazos_${asientoId}">
            <label class="form-check-label" for="brazos_${asientoId}">Con menor en brazos</label>
            </div>
            <div class="form-check mb-2">
            <input class="form-check-input" type="checkbox" id="esMenor_${asientoId}">
            <label class="form-check-label" for="esMenor_${asientoId}">Es menor de edad</label>
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
        // Validar que todos los campos estén completos antes de guardar
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
        // Inicialización general si es necesaria
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

        // Llenar campos básicos
        Object.entries(campos).forEach(([campo, valor]) => {
            const elemento = document.getElementById(`${campo}_${asiento}`);
            if (elemento) elemento.value = valor;
        });

        // Fecha de nacimiento
        if (datos.f_nacimiento) {
            const fechaElement = document.getElementById(`fechaNacimientoNuevo_${asiento}`);
            if (fechaElement) {
                fechaElement.value = moment(datos.f_nacimiento).format("YYYY-MM-DD");
                this.validarEdad(asiento);
            }
        }

        // Sexo
        if (datos.sexo != null) {
            const masculino = document.getElementById(`sexoMasculino_${asiento}`);
            const femenino = document.getElementById(`sexoFemenino_${asiento}`);
            if (masculino && femenino) {
                masculino.checked = datos.sexo === 1;
                femenino.checked = datos.sexo !== 1;
            }
        }

        // Trigger validation check after filling data
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
        // Limpiar temporizador existente si lo hay
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

        // 🔓 LIBERAR ASIENTOS CUANDO SE AGOTE EL TIEMPO
        console.log('⏰ Tiempo agotado - Liberando asientos automáticamente...');

        try {
            // Liberar todos los asientos seleccionados
            await SeatManager.liberarTodosLosAsientos();

            // Limpiar datos locales
            sessionStorage.removeItem('ventas');

            // Mostrar mensaje al usuario
            toastr.error('Tiempo agotado. Los asientos han sido liberados automáticamente.', 'TIEMPO AGOTADO');

            // Opcional: Resetear sistema después de un delay
            setTimeout(() => {
                App.resetearSistemaCompleto();
                NavigationManager.updateFormVisibility();
                toastr.info('Sistema reiniciado. Puede realizar una nueva búsqueda.');
            }, 3000);

        } catch (error) {
            console.error('❌ Error liberando asientos por tiempo agotado:', error);
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
        console.log('🛑 Deteniendo todos los temporizadores activos...');
        this.intervals.forEach((intervalo, sufijo) => {
            clearInterval(intervalo);
            console.log(`⏹️ Temporizador ${sufijo} detenido`);
        });
        this.intervals.clear();
    }
};
// =============================================================================
// GESTOR DE RECARGA/CIERRE DE PÁGINA
// =============================================================================

const PageUnloadManager = {
    init() {
        // Detectar recarga/cierre de página
        window.addEventListener('beforeunload', (event) => {
            this.handlePageUnload(event);
        });

        // También detectar cuando se va de la página (por si acaso)
        window.addEventListener('unload', () => {
            this.cleanupOnExit();
        });

        console.log('📄 PageUnloadManager inicializado (listeners limpiados)');
    },

    handlePageUnload(event) {
        const hayProgreso = this.verificarProgreso();

        if (hayProgreso) {
            // Mostrar mensaje de confirmación del navegador
            event.preventDefault();
            event.returnValue = '¿Estás seguro de que quieres salir? Perderás tu progreso de reserva.';

            // Ejecutar limpieza en segundo plano
            this.cleanupOnExit();

            return '¿Estás seguro de que quieres salir? Perderás tu progreso de reserva.';
        }
    },

    verificarProgreso() {
        // ✅ CRITERIO CORREGIDO: Priorizar asientos seleccionados en memoria
        const hayAsientosSeleccionados = SeatManager && SeatManager.asientosSeleccionados && SeatManager.asientosSeleccionados.size > 0;

        const ventasStorage = sessionStorage.getItem('ventas');
        const hayVentas = ventasStorage && Object.keys(JSON.parse(ventasStorage)).length > 0;

        console.log(`📊 Verificación de progreso (PageUnload):`, {
            asientosSeleccionados: hayAsientosSeleccionados,
            cantidadAsientos: SeatManager?.asientosSeleccionados?.size || 0,
            ventasStorage: !!hayVentas
        });

        return hayAsientosSeleccionados || hayVentas;
    },

    cleanupOnExit() {
        try {
            // ✅ PRIORIDAD 1: Obtener asientos desde memoria (PRINCIPAL)
            const hayAsientosSeleccionados = SeatManager && SeatManager.asientosSeleccionados && SeatManager.asientosSeleccionados.size > 0;

            // ✅ PRIORIDAD 2: Obtener asientos desde sessionStorage 
            const ventasStorage = sessionStorage.getItem('ventas');
            const hayVentas = ventasStorage && Object.keys(JSON.parse(ventasStorage)).length > 0;

            if (hayAsientosSeleccionados || hayVentas) {
                console.log('🔓 Liberando asientos al salir...');

                // Recopilar todos los asientos para liberar
                const asientosParaLiberar = new Set();

                // ✅ PRIORIDAD: Asientos desde memoria primero
                if (hayAsientosSeleccionados) {
                    console.log(`📍 Agregando ${SeatManager.asientosSeleccionados.size} asientos desde memoria`);
                    SeatManager.asientosSeleccionados.forEach(id => asientosParaLiberar.add(id));
                }

                // Asientos desde sessionStorage (adicionales)
                if (hayVentas) {
                    const ventas = JSON.parse(ventasStorage);
                    const asientosStorage = Object.keys(ventas);
                    console.log(`📍 Agregando ${asientosStorage.length} asientos desde storage`);
                    asientosStorage.forEach(id => asientosParaLiberar.add(id));
                }

                // Usar sendBeacon para asegurar que llegue al servidor
                const asientosArray = Array.from(asientosParaLiberar);
                console.log(`🔓 Total de asientos para liberar: ${asientosArray.length}`, asientosArray);

                asientosArray.forEach(asientoId => {
                    SeatManager.marcarAsientoComoDisponible(asientoId)
                });


                console.log(`✅ ${asientosArray.length} asientos enviados para liberación`);
            }

            // Limpiar sessionStorage al final
            sessionStorage.removeItem('ventas');
            console.log('🧹 SessionStorage limpiado');

        } catch (error) {
            console.error('❌ Error en limpieza al salir:', error);
        }
    }
};
// =============================================================================
// GESTIÓN DE PAGO CON FORMULARIO DINÁMICO (PARTE 1)
// =============================================================================

const PaymentManager = {
    metodosPagoBD: null,
    datosContacto: {},

    async initialize() {
        console.log('🚀 Inicializando PaymentManager...');

        // Verificar que los elementos existan
        const selector = document.getElementById("selector_metodo_pago");

        if (!selector) {
            console.error('❌ No se encontró el elemento selector_metodo_pago');
            return;
        }

        console.log('✅ Elementos de pago encontrados');

        try {
            // Cargar métodos de pago desde la API
            this.metodosPagoBD = await this.obtenerMetodosPagoDesdeAPI();
            console.log('📦 Métodos de pago cargados:', this.metodosPagoBD);

            this.poblarTiposPago();
            this.configurarEventos();
            this.generarFormularioContactoDinamico();

            console.log('✅ PaymentManager inicializado correctamente');
        } catch (error) {
            console.error('❌ Error inicializando sistema de pago:', error);
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
                return this.obtenerMetodosPagoMock(); // Fallback al mock
            }
        } catch (err) {
            console.error('Error al cargar métodos de pago:', err);
            toastr.error("Error al cargar los métodos de pago: " + (err.message || err));
            return this.obtenerMetodosPagoMock(); // Fallback al mock
        }
    },
    /*
        obtenerMetodosPagoMock() {
            return {
                "1": [
                    {
                        id_metodo: "1",
                        tipo_metodo: "Tarjeta",
                        metodo: "Visa",
                        qr: null,
                        logo: "visa-logo.png"
                    },
                    {
                        id_metodo: "2",
                        tipo_metodo: "Tarjeta",
                        metodo: "Mastercard",
                        qr: null,
                        logo: "mastercard-logo.png"
                    }
                ],
                "2": [
                    {
                        id_metodo: "3",
                        tipo_metodo: "Billetera virtual",
                        metodo: "Yape",
                        qr: "/static/img/qr-yape.png",
                        logo: "yape-logo.png"
                    },
                    {
                        id_metodo: "4",
                        tipo_metodo: "Billetera virtual",
                        metodo: "Plin",
                        qr: "/static/img/qr-plin.png",
                        logo: "plin-logo.png"
                    }
                ],
                "3": [
                    {
                        id_metodo: "5",
                        tipo_metodo: "Efectivo",
                        metodo: "Pago en ventanilla",
                        qr: null,
                        logo: "efectivo-logo.png"
                    }
                ]
            };
        },
    */
    generarFormularioContactoDinamico() {
        const accordionBody = document.querySelector('#collapseContacto .accordion-body');
        if (!accordionBody) return;

        accordionBody.innerHTML = `
            <div class="row g-3">
                <!-- Selector de tipo de comprobante -->
                <div class="col-md-12">
                    <label for="tipo_comprobante" class="form-label">Tipo de comprobante</label>
                    <select id="tipo_comprobante" class="form-select">
                        <option value=1>Boleta</option>
                        <option value=2>Factura</option>
                    </select>
                </div>
                
                <!-- Contenido dinámico según tipo de comprobante -->
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

        // Inicializar con boleta por defecto
        this.renderizarCamposComprobante('1');
        this.configurarEventosComprobante();
    },
    // =============================================================================
    // GESTIÓN DE PAGO CON FORMULARIO DINÁMICO (PARTE 2)
    // =============================================================================

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
                    <div class="col-md-12">
                        <label for="email_contacto" class="form-label">Correo electrónico *</label>
                        <input type="email" id="email_contacto" class="form-control" required>
                    </div>
                    <div class="col-md-6">
                        <label for="tipo_documento_contacto" class="form-label">Tipo de documento *</label>
                        <select id="tipo_documento_contacto" class="form-select">
                            <option value="DNI">DNI</option>
                            <option value="CE">Carné de Extranjería</option>
                        </select>
                    </div>
                    <div class="col-md-6">
                        <label for="numero_documento_contacto" class="form-label">Número de documento *</label>
                        <input type="text" id="numero_documento_contacto" class="form-control" required>
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

        // Configurar eventos de validación y RENIEC/SUNAT
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
            // Consultar RENIEC para DNI (8 dígitos) o CE (9-12 dígitos)
            const tipoDoc = document.getElementById("tipo_documento_contacto").value;
            if ((tipoDoc === 'DNI' && numeroDoc.length === 8) ||
                (tipoDoc === 'CE' && numeroDoc.length >= 9 && numeroDoc.length <= 12)) {
                await this.consultarReniecContacto(tipoDoc, numeroDoc);
            }
        } else if (tipoComprobante == '2') {
            // Consultar SUNAT para RUC (11 dígitos)
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

                // Llenar campos automáticamente
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
            console.warn("Error consultando RENIEC para contacto:", err);
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

                // Llenar campos automáticamente
                const razonSocial = document.getElementById("razon_social_contacto");
                const direccion = document.getElementById("direccion_contacto");
                const telefono = document.getElementById("telefono_contacto");

                if (razonSocial) razonSocial.value = datos.razonSocial || datos.nombre_razon_social || "";
                if (direccion) direccion.value = datos.direccion || datos.direccion_completa || "";
                if (telefono) telefono.value = datos.telefono || "";

                toastr.success("Datos de la empresa cargados automáticamente");
            }
        } catch (err) {
            console.warn("Error consultando SUNAT para contacto:", err);
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
                const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
                esValido = emailRegex.test(valor);
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
        // Validar todos los campos de contacto
        if (!this.validarFormularioContactoCompleto()) {
            toastr.error("Por favor complete todos los campos requeridos correctamente");
            return;
        }

        // Validar que se hayan completado todos los datos de pasajeros
        if (!this.validarDatosPasajerosCompletos()) {
            toastr.error("Por favor complete los datos de todos los pasajeros");
            return;
        }

        // Si todo está correcto, abrir sección de pago
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
        // Obtener todas las ventas guardadas
        const ventas = JSON.parse(sessionStorage.getItem("ventas") || "{}");

        if (Object.keys(ventas).length === 0) {
            toastr.warning("No hay asientos seleccionados");
            return false;
        }

        for (const asientoId in ventas) {
            const venta = ventas[asientoId];

            // Validar campos obligatorios (excepto checkboxes)
            const camposObligatorios = ['numDoc', 'nombres', 'apellidoPaterno', 'apellidoMaterno', 'telefono', 'correo'];

            for (const campo of camposObligatorios) {
                if (!venta[campo] || venta[campo].trim() === '') {
                    toastr.warning(`Complete los datos del pasajero en el asiento ${asientoId}`);
                    return false;
                }
            }
        }

        return true;
    },

    poblarTiposPago() {
        const selector = document.getElementById("selector_metodo_pago");
        if (!selector) return;

        // Limpiar opciones existentes (excepto la primera)
        selector.innerHTML = '<option value="">Seleccione</option>';

        // Poblar combo de tipos
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

        // Evento para cambio de tipo de pago
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

        // Crear selector de métodos específicos
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

        // Mostrar contenido del primer método por defecto
        this.renderizarContenidoMetodo(metodos[0], tipoMetodo);

        // Configurar evento para cambios de método específico
        selectMetodo.addEventListener("change", (e) => {
            const metodoSeleccionado = metodos.find(m => m.id_metodo == e.target.value);
            if (metodoSeleccionado) {
                this.renderizarContenidoMetodo(metodoSeleccionado, tipoMetodo);
            }
        });

        // Agregar botón de finalizar pago
        this.agregarBotonFinalizarPago(contenedor);
    },

    renderizarContenidoMetodo(metodo, tipoMetodo) {
        const contenedor = document.getElementById("contenido_pago_dinamico");

        // Remover contenido anterior del método
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
                        <li>Presente este código de reserva: <strong id="codigo_reserva">${this.generarCodigoReserva()}</strong></li>
                        <li>El boleto será válido una vez confirmado el pago</li>
                    </ul>
                </div>
                <div class="mb-3">
                    <label class="form-label">Código promocional (opcional)</label>
                    <input id="codigo_promocional_efectivo" class="form-control" placeholder="Ingrese código promocional">
                </div>
            `;
        }

        // Insertar antes del botón de finalizar pago
        const botonFinalizar = document.getElementById("btn_finalizar_pago");
        if (botonFinalizar) {
            contenedor.insertBefore(divExtra, botonFinalizar.parentElement);
        } else {
            contenedor.appendChild(divExtra);
        }
    },

    agregarBotonFinalizarPago(contenedor) {
        // Verificar si ya existe el botón
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

        // Configurar evento del botón
        document.getElementById("btn_finalizar_pago").addEventListener("click", async () => {
            const tipoMetodo = document.getElementById("selector_metodo_pago").value;
            const metodoPago = document.getElementById("metodo_pago_especifico").value; //document.getElementById("selector_metodo_pago").value;
            let nombreTipoMetodo = await obtenerNombreTipoMetodo(tipoMetodo)
            let nombreMetodo = await obtenerNombreMetodo(metodoPago)


            if (nombreMetodo == "tarjeta de credito" || nombreMetodo == "tarjeta") {
               
                this.procesarPago();
            } else if (nombreTipoMetodo == "efectivo" && nombreMetodo == "efectivo") {
               
                this.procesarReserva();
            } else {
                console.log(nombreTipoMetodo)
                console.log(nombreMetodo)
                console.error("Espacio para pasaje libre en un futuro");
            }
        });
    },

    async procesarPago() {
        if (!this.validarFormularioCompleto()) {
            toastr.error("Por favor complete todos los campos requeridos");
            return;
        }

        const datosCompletos = this.capturarDatosPago();

        // Mostrar loader
        this.mostrarLoader();

        try {
            // Llamada al servidor
            const response = await fetch(CONFIG.RUTAS.PROCESAR_PAGO, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(datosCompletos)
            });

            const resultado = await response.json();

            // Ocultar loader
            this.ocultarLoader();

            if (resultado.Status === 'success') {
                this.mostrarPagoExitoso(resultado);
            } else {
                throw new Error(resultado.Msj || 'Error en el procesamiento del pago');
            }

        } catch (error) {
            this.ocultarLoader();
            toastr.error("Error al procesar el pago: " + error.message);
            console.error('Error procesando pago:', error);
        }
    },

    async procesarReserva() {
        if (!this.validarFormularioCompleto()) {
            toastr.error("Por favor complete todos los campos requeridos");
            return;
        }

        const datosCompletos = this.capturarDatosPago();

        // Mostrar loader
        this.mostrarLoader();

        try {
            // Llamada al servidor
            const response = await fetch(CONFIG.RUTAS.PROCESAR_RESERVA, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(datosCompletos)
            });

            const resultado = await response.json();

            // Ocultar loader
            this.ocultarLoader();

            if (resultado.Status === 'success') {
                this.mostrarPagoExitoso(resultado);
            } else {
                throw new Error(resultado.Msj || 'Error en el procesamiento del pago');
            }

        } catch (error) {
            this.ocultarLoader();
            toastr.error("Error al procesar el pago: " + error.message);
            console.error('Error procesando pago:', error);
        }
    },

    validarFormularioCompleto() {
        // Validar contacto
        if (!this.validarFormularioContactoCompleto()) return false;

        // Validar método de pago seleccionado
        const tipoMetodo = document.getElementById("selector_metodo_pago").value;
        if (!tipoMetodo) {
            toastr.warning("Debe seleccionar un método de pago");
            return false;
        }

        // Validar campos específicos del método de pago
        return this.validarCamposMetodoPago();
    },

    validarCamposMetodoPago() {
        const metodoEspecifico = document.getElementById("metodo_pago_especifico");
        if (!metodoEspecifico) return true;

        const metodoSeleccionado = metodoEspecifico.options[metodoEspecifico.selectedIndex].text;

        // Validar campos de tarjeta si es necesario
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

            // Validar formato de número de tarjeta (básico)
            if (!/^\d{4}\s?\d{4}\s?\d{4}\s?\d{4}$/.test(numeroTarjeta.value.replace(/\s/g, ''))) {
                toastr.warning("Formato de número de tarjeta inválido");
                return false;
            }
        }

        return true;
    },

    capturarDatosPago() {
        const tipoComprobante = document.getElementById("tipo_comprobante").value;

        // Capturar datos de contacto según tipo de comprobante
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

        // Capturar datos del método de pago
        const tipoMetodo = document.getElementById("selector_metodo_pago").value;
        const metodoEspecifico = document.getElementById("metodo_pago_especifico")?.value;

        const datosPago = {
            tipo_metodo: tipoMetodo,
            metodo_especifico: metodoEspecifico,
            timestamp: new Date().toISOString()
        };

        // Capturar datos específicos según el método
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

    mostrarLoader() {
        // Crear overlay de loading
        const overlay = document.createElement('div');
        overlay.id = 'payment-loader-overlay';
        overlay.style.cssText = `
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(0,0,0,0.7);
            display: flex;
            justify-content: center;
            align-items: center;
            z-index: 9999;
        `;

        overlay.innerHTML = `
            <div style="text-align: center; color: white;">
                <div class="spinner-border text-light" style="width: 4rem; height: 4rem;" role="status">
                    <span class="visually-hidden">Cargando...</span>
                </div>
                <h4 class="mt-3">Procesando pago...</h4>
                <p class="text-muted">Por favor espere mientras confirmamos su transacción</p>
            </div>
        `;

        document.body.appendChild(overlay);

        // Deshabilitar botón de pago
        const boton = document.getElementById("btn_finalizar_pago");
        if (boton) {
            boton.disabled = true;
            boton.innerHTML = '<i class="fas fa-spinner fa-spin me-2"></i>Procesando...';
        }
    },

    ocultarLoader() {
        const overlay = document.getElementById('payment-loader-overlay');
        if (overlay) overlay.remove();

        // Rehabilitar botón
        const boton = document.getElementById("btn_finalizar_pago");
        if (boton) {
            boton.disabled = false;
            boton.innerHTML = '<i class="fas fa-credit-card me-2"></i>Finalizar Pago';
        }
    },
    mostrarPagoExitoso(resultado) {
        // Crear overlay de éxito
        const overlay = document.createElement('div');
        overlay.id = 'payment-success-overlay';
        overlay.style.cssText = `
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: linear-gradient(135deg, #d4f8d4 0%, #a8e6a8 100%);
            display: flex;
            justify-content: center;
            align-items: center;
            z-index: 9999;
            animation: fadeIn 0.5s ease-in;
        `;

        overlay.innerHTML = `
            <div style="text-align: center; animation: bounceIn 0.8s ease-out;">
                <div style="
                    width: 120px;
                    height: 120px;
                    border-radius: 50%;
                    background: #28a745;
                    margin: 0 auto 30px;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    animation: checkmarkAnimation 0.6s ease-in-out 0.3s both;
                ">
                    <i class="fas fa-check" style="color: white; font-size: 60px;"></i>
                </div>
                <h1 style="color: #155724; margin-bottom: 20px; font-weight: bold;">¡Pago Confirmado!</h1>
                <h4 style="color: #155724; margin-bottom: 15px;">Código de confirmación: <strong>${resultado.codigo_confirmacion || 'PAY-' + Date.now()}</strong></h4>
                <p style="color: #155724; font-size: 18px; margin-bottom: 30px;">
                    Su reserva ha sido procesada exitosamente.<br>
                    Recibirá un correo de confirmación en ${this.datosContacto.email}
                </p>
                <button id="btn_nueva_reserva" class="btn btn-success btn-lg" style="margin-right: 15px;">
                    <i class="fas fa-plus me-2"></i>Nueva Reserva
                </button>
                <button id="btn_descargar_boleto" class="btn btn-outline-success btn-lg">
                    <i class="fas fa-download me-2"></i>Descargar Boleto
                </button>
            </div>
        `;

        // Agregar estilos de animación
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

        // Configurar eventos de los botones
        document.getElementById('btn_nueva_reserva').addEventListener('click', () => {
            this.iniciarNuevaReserva();
        });

        document.getElementById('btn_descargar_boleto').addEventListener('click', () => {
            this.descargarBoleto(resultado);
        });

        // Limpiar datos de la reserva actual
        this.limpiarDatosReserva();
    },

    iniciarNuevaReserva() {
        // Remover overlay
        const overlay = document.getElementById('payment-success-overlay');
        if (overlay) overlay.remove();

        // Resetear sistema completo
        App.resetearSistemaCompleto();
        NavigationManager.updateFormVisibility();

        // Scroll hacia arriba
        window.scrollTo({ top: 0, behavior: 'smooth' });

        toastr.success('Listo para una nueva reserva');
    },

    descargarBoleto(resultado) {
        // Aquí implementarías la descarga del boleto
        // Por ahora, solo simulamos
        toastr.info('Preparando descarga del boleto...');

        // Simular descarga
        setTimeout(() => {
            const link = document.createElement('a');
            link.href = '#'; // En realidad sería la URL del PDF
            link.download = `boleto-${resultado.codigo_confirmacion || 'reserva'}.pdf`;
            link.click();
            toastr.success('Boleto descargado exitosamente');
        }, 1500);
    },

    limpiarDatosReserva() {
        // Limpiar sessionStorage
        sessionStorage.removeItem('ventas');
        sessionStorage.removeItem('datos_pago');

        // Resetear estado
        this.datosContacto = {};

        console.log('🧹 Datos de reserva limpiados tras pago exitoso');
    },

    limpiarFormularioPago() {
        // Resetear selector de comprobante a boleta
        const tipoComprobante = document.getElementById("tipo_comprobante");
        if (tipoComprobante) {
            tipoComprobante.value = '1';
        }

        // Regenerar formulario con boleta por defecto
        this.renderizarCamposComprobante('1');

        // Resetear selectors de pago
        const selectorTipo = document.getElementById("selector_metodo_pago");
        if (selectorTipo) {
            selectorTipo.selectedIndex = 0;
        }

        // Limpiar contenido dinámico de pago
        const contenedorDinamico = document.getElementById("contenido_pago_dinamico");
        if (contenedorDinamico) {
            contenedorDinamico.innerHTML = '';
        }

        console.log('💳 Formulario de pago limpiado');
    },

    mostrarErrorCampo(elemento, mensaje) {
        if (!elemento) return;

        elemento.classList.add('is-invalid');

        // Remover mensaje anterior si existe
        const errorAnterior = elemento.parentNode.querySelector('.invalid-feedback');
        if (errorAnterior) errorAnterior.remove();

        // Agregar nuevo mensaje
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

    generarCodigoReserva() {
        const timestamp = Date.now().toString(36);
        const random = Math.random().toString(36).substr(2, 5);
        return `RES-${timestamp}-${random}`.toUpperCase();
    }

};
// =============================================================================
// FORM VALIDATION MANAGER - VALIDACIÓN EN TIEMPO REAL
// =============================================================================

const FormValidationManager = {
    init() {
        this.setupRealTimeValidation();
        console.log('📝 FormValidationManager inicializado');
    },

    // ✅ CONFIGURAR VALIDACIÓN EN TIEMPO REAL
    setupRealTimeValidation() {
        // ✅ CORRECCIÓN: Solo 'input' para validación mientras escribe, 'change' para selects
        $(document).on('input', '[id^="accordionPasajeros_"] input', (e) => {
            const $element = $(e.target);
            const sufijo = this.getSufijoFromElement(e.target);

            if (sufijo) {
                // Validar inmediatamente mientras escribe
                this.validarCampoIndividual($element);

                // Validar el formulario completo sin delay
                this.validarFormularioCompleto(sufijo);
            }
        });

        // Para selects usar 'change'
        $(document).on('change', '[id^="accordionPasajeros_"] select', (e) => {
            const $element = $(e.target);
            const sufijo = this.getSufijoFromElement(e.target);

            if (sufijo) {
                this.validarCampoIndividual($element);
                this.validarFormularioCompleto(sufijo);
            }
        });

        // Observer para detectar cuando se carga dinámicamente el formulario
        const observer = new MutationObserver((mutations) => {
            mutations.forEach((mutation) => {
                mutation.addedNodes.forEach((node) => {
                    if (node.nodeType === 1 && node.matches && node.matches('[id^="accordionPasajeros_"]')) {
                        const sufijo = node.id.replace('accordionPasajeros_', '');
                        setTimeout(() => {
                            this.setupFormValidation(sufijo);
                        }, 100);
                    }
                });
            });
        });

        observer.observe(document.body, { childList: true, subtree: true });
    },

    // ✅ OBTENER SUFIJO DESDE ELEMENTO
    getSufijoFromElement(element) {
        const closest = $(element).closest('[id^="accordionPasajeros_"]');
        if (closest.length) {
            const id = closest.attr('id');
            return id.replace('accordionPasajeros_', '');
        }
        return null;
    },

    // ✅ CONFIGURAR VALIDACIÓN PARA UN FORMULARIO ESPECÍFICO
    setupFormValidation(sufijo) {
        const accordion = $(`#accordionPasajeros_${sufijo}`);
        if (!accordion.length) return;

        console.log(`🔧 Configurando validación para: ${sufijo}`);

        // Encontrar y configurar el botón de guardar datos
        const botonGuardar = accordion.closest('.col-md-12').find('button[onclick*="acabar"]');
        if (botonGuardar.length) {
            // Siempre mostrar "Guardar datos"
            botonGuardar.html('<i class="fas fa-save"></i> Guardar datos');

            // Agregar clases Bootstrap para mejor UX
            botonGuardar.removeClass('btn-outline-primary').addClass('btn-outline-secondary');
            botonGuardar.prop('disabled', true);
        }

        // Validar estado inicial después de un pequeño delay
        setTimeout(() => {
            this.validarFormularioCompleto(sufijo);
        }, 200);
    },

    // ✅ VALIDAR CAMPO INDIVIDUAL EN TIEMPO REAL
    validarCampoIndividual($element) {
        const valor = $element.val()?.trim();
        const tipo = $element.attr('type') || ($element.is('select') ? 'select' : 'text');
        const nombre = $element.attr('name') || $element.attr('placeholder') || 'Campo';

        console.log(`⌨️ Validando en tiempo real: ${nombre} = "${valor}"`);

        const validacion = this.validarCampo($element, valor, tipo);

        if (!validacion.valido) {
            this.marcarCampoInvalido($element, validacion.mensaje);
            console.log(`❌ ${nombre}: ${validacion.mensaje}`);
        } else {
            this.marcarCampoValido($element);
            console.log(`✅ ${nombre}: Válido`);
        }

        return validacion.valido;
    },

    // ✅ VALIDAR FORMULARIO COMPLETO PARA UN SUFIJO
    validarFormularioCompleto(sufijo) {
        const accordion = $(`#accordionPasajeros_${sufijo}`);
        if (!accordion.length) return false;

        let todoValido = true;
        let camposRequeridos = 0;
        let camposValidos = 0;

        // Obtener todos los inputs/selects REQUERIDOS del acordeón
        const camposRequeridos_elementos = accordion.find('input[required], select[required]');
        camposRequeridos = camposRequeridos_elementos.length;

        console.log(`🔍 Validando ${sufijo}: ${camposRequeridos} campos requeridos`);

        camposRequeridos_elementos.each((index, element) => {
            const $element = $(element);
            const valor = $element.val()?.trim();
            const tipo = $element.attr('type') || ($element.is('select') ? 'select' : 'text');

            // Validar cada campo
            const validacion = this.validarCampo($element, valor, tipo);

            if (validacion.valido) {
                camposValidos++;
                this.marcarCampoValido($element);
            } else {
                todoValido = false;
                this.marcarCampoInvalido($element, validacion.mensaje);
            }
        });

        console.log(`📊 ${sufijo}: ${camposValidos}/${camposRequeridos} campos válidos`);

        // Actualizar estado del botón
        this.actualizarBotonGuardar(sufijo, todoValido);

        return todoValido;
    },

    // ✅ VALIDAR CAMPO INDIVIDUAL CON REGLAS ESPECÍFICAS
    validarCampo($element, valor, tipo) {
        const nombre = $element.attr('name') || $element.attr('id') || 'Campo';
        const placeholder = $element.attr('placeholder') || '';

        // Campo requerido vacío
        if (!valor) {
            return { valido: false, mensaje: 'Este campo es obligatorio' };
        }

        // Validaciones específicas por tipo y nombre
        switch (tipo) {
            case 'email':
                const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
                if (!emailRegex.test(valor)) {
                    return { valido: false, mensaje: 'Email inválido (ej: usuario@dominio.com)' };
                }
                break;

            case 'text':
                // Validación por nombre/placeholder
                if (nombre.toLowerCase().includes('nombre') || placeholder.toLowerCase().includes('nombre')) {
                    if (valor.length < 2) {
                        return { valido: false, mensaje: 'Mínimo 2 caracteres' };
                    }
                    if (!/^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$/.test(valor)) {
                        return { valido: false, mensaje: 'Solo letras y espacios' };
                    }
                }

                if (nombre.toLowerCase().includes('dni') || placeholder.toLowerCase().includes('dni')) {
                    if (!/^\d{8}$/.test(valor)) {
                        return { valido: false, mensaje: 'DNI debe tener exactamente 8 dígitos' };
                    }
                }

                if (nombre.toLowerCase().includes('telefono') || placeholder.toLowerCase().includes('telefono')) {
                    if (!/^\d{9}$/.test(valor)) {
                        return { valido: false, mensaje: 'Teléfono debe tener 9 dígitos' };
                    }
                }
                break;

            case 'date':
                const fecha = new Date(valor);
                if (isNaN(fecha.getTime())) {
                    return { valido: false, mensaje: 'Fecha inválida' };
                }

                // Validar que no sea fecha futura para fecha de nacimiento
                if (nombre.toLowerCase().includes('nacimiento')) {
                    const hoy = new Date();
                    if (fecha > hoy) {
                        return { valido: false, mensaje: 'Fecha no puede ser futura' };
                    }
                }
                break;

            case 'select':
                if (!valor || valor === '' || valor === '0' || valor === 'Seleccionar') {
                    return { valido: false, mensaje: 'Debe seleccionar una opción' };
                }
                break;
        }

        return { valido: true, mensaje: '' };
    },

    // ✅ MARCAR CAMPO COMO INVÁLIDO
    marcarCampoInvalido($element, mensaje) {
        $element.removeClass('is-valid').addClass('is-invalid');

        // Buscar o crear feedback
        let feedback = $element.siblings('.invalid-feedback');
        if (!feedback.length) {
            feedback = $('<div class="invalid-feedback"></div>');
            $element.after(feedback);
        }
        feedback.text(mensaje);
    },

    // ✅ MARCAR CAMPO COMO VÁLIDO
    marcarCampoValido($element) {
        $element.removeClass('is-invalid').addClass('is-valid');
        $element.siblings('.invalid-feedback').remove();
    },

    // ✅ ACTUALIZAR BOTÓN GUARDAR
    actualizarBotonGuardar(sufijo, todoValido) {
        const accordion = $(`#accordionPasajeros_${sufijo}`);
        const boton = accordion.closest('.col-md-12').find('button[onclick*="acabar"]');

        if (boton.length) {
            // Texto siempre igual
            boton.html('<i class="fas fa-save"></i> Guardar datos');

            if (todoValido) {
                boton.prop('disabled', false)
                    .removeClass('btn-outline-secondary')
                    .addClass('btn-outline-primary');
            } else {
                boton.prop('disabled', true)
                    .removeClass('btn-outline-primary')
                    .addClass('btn-outline-secondary');
            }
        }
    },

    // ✅ VERIFICAR SI UN FORMULARIO ESTÁ COMPLETAMENTE VÁLIDO
    estanDatosValidados(sufijo) {
        // Validar en tiempo real el estado actual del formulario
        return this.validarFormularioCompleto(sufijo);
    },

    // ✅ VALIDAR ANTES DE NAVEGAR (VALIDACIÓN REAL)
    puedeNavegar(sufijo) {
        const datosValidados = this.estanDatosValidados(sufijo);

        if (!datosValidados) {
            Swal.fire({
                title: "Datos incompletos o incorrectos",
                text: "Debes completar correctamente todos los campos requeridos antes de continuar.",
                icon: "warning",
                confirmButtonText: "Entendido",
                confirmButtonColor: '#3085d6'
            });
            return false;
        }

        return true;
    },

    // ✅ LIMPIAR VALIDACIONES
    limpiarValidaciones(sufijo) {
        const accordion = $(`#accordionPasajeros_${sufijo}`);
        accordion.find('.is-valid, .is-invalid').removeClass('is-valid is-invalid');
        accordion.find('.invalid-feedback').remove();
    }
};

const ClearManager = {
    
}

const App = {
    init() {
        this.configurarEventosGlobales();
        this.inicializarComponentes();
        NavigationManager.inicializarEstadoPorDefecto();
        PageUnloadManager.init();
        FormValidationManager.init()
    },

    // =============================================================================
    // FUNCIONES DE RESETEO
    // =============================================================================

    resetearSistemaCompletoSinRutas() {
        console.log('🔄 Reseteando sistema completo (preservando rutas)...');

        try {
            // 1. Limpiar sessionStorage
            sessionStorage.removeItem('ventas');

            // 2. Resetear asientos seleccionados
            if (typeof SeatManager !== 'undefined') {
                SeatManager.asientosSeleccionados.clear();
            }

            // 3. Limpiar contenedores de itinerarios
            const contenedorIda = document.getElementById('contenedor_viajes_ida');
            const contenedorVuelta = document.getElementById('contenedor_viajes_vuelta');

            if (contenedorIda) contenedorIda.innerHTML = '';
            if (contenedorVuelta) contenedorVuelta.innerHTML = '';

            // 4. Resetear estado de la aplicación
            AppState.currentStep = 0;
            AppState.maxStep = 0;
            AppState.itinerarioRegreso = null;

            // ✅ NUEVO: Limpiar validaciones de formularios
            if (typeof FormValidationManager !== 'undefined') {
                AppState.validacionFormularios = {};
                FormValidationManager.limpiarValidaciones('ida');
                FormValidationManager.limpiarValidaciones('vuelta');
            }

            // 5. Limpiar temporizadores activos
            if (typeof TimerManager !== 'undefined') {
                TimerManager.clearAllTimers();
            }

            // 6. Resetear formularios de pasajeros
            document.querySelectorAll('[id^="accordionPasajeros_"]').forEach(accordion => {
                accordion.innerHTML = '';
            });

            // 7. Ocultar contenedores de datos de pasajeros
            document.querySelectorAll('[id^="contenido_datos_"]').forEach(contenedor => {
                contenedor.classList.add('d-none');
            });

            console.log('✅ Sistema reseteado correctamente (rutas preservadas)');

        } catch (error) {
            console.error('❌ Error al resetear sistema:', error);
        }
    },

    resetearSistemaCompleto() {
        console.log('🔄 Reseteando sistema completo...');

        // 1. Limpiar estado de la aplicación
        AppState.resetProgress();

        // 2. Limpiar almacenamiento del navegador
        sessionStorage.removeItem('ventas');
        sessionStorage.removeItem('datos_pago');
        sessionStorage.clear();

        // 3. Limpiar formularios
        this.limpiarFormularios();

        // 4. Limpiar contenedores dinámicos
        this.limpiarContenedoresDinamicos();

        // 5. Detener todos los temporizadores activos
        TimerManager.detenerTodos();

        // 6. Resetear asientos seleccionados
        this.limpiarAsientosSeleccionados();

        // 7. Limpiar formulario de pago
        if (typeof PaymentManager !== 'undefined') {
            PaymentManager.limpiarFormularioPago();
        }

        // 8. Resetear selección de asientos
        if (typeof SeatManager !== 'undefined') {
            SeatManager.asientosSeleccionados.clear();
        }

        console.log('✅ Sistema completamente limpio');
    },

    limpiarFormularios() {
        // Limpiar formulario principal de búsqueda
        $('#cbx_Ciudades').val(null).trigger('change');
        $('input[name="fecha_ida"]').val('');
        $('input[name="fecha_vuelta"]').val('');

        // Limpiar cualquier formulario de pasajeros
        $('input[type="text"], input[type="email"], input[type="date"]').val('');
        $('input[type="checkbox"], input[type="radio"]').prop('checked', false);
        $('select').prop('selectedIndex', 0);
    },

    limpiarContenedoresDinamicos() {
        // Limpiar contenedores de viajes
        ['contenedor_viajes_ida', 'contenedor_viajes_vuelta'].forEach(id => {
            const contenedor = document.getElementById(id);
            if (contenedor) contenedor.innerHTML = '';
        });

        // Limpiar acordeones de pasajeros
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

        // Limpiar matrices de asientos
        ['ida', 'vuelta'].forEach(sufijo => {
            const matrices = document.querySelectorAll(`[id^="matrizContainer_"][id$="_${sufijo}"]`);
            matrices.forEach(m => m.innerHTML = '');
        });
    },

    limpiarAsientosSeleccionados() {
        // Remover clase de asientos seleccionados
        document.querySelectorAll('.asiento-seleccionado').forEach(asiento => {
            asiento.classList.remove('asiento-seleccionado');
            asiento.style.backgroundColor = '';
            asiento.style.color = '';
        });
    },

    configurarEventosGlobales() {
        // Evento para botones "Siguiente"
        $(document).on('click', '.btn-siguiente', () => {
            NavigationManager.goToNextStep();
        });

        // Hacer funciones globales accesibles
        window.buscarYMostrarItinerario = SearchManager.buscarYMostrarItinerario.bind(SearchManager);
        window.acabarPrimerItinerario = NavigationManager.confirmarDatosIda.bind(NavigationManager);
        window.acabarSegundoItinerario = NavigationManager.confirmarDatosRegreso.bind(NavigationManager);
        window.volverAItinerarioIda = NavigationManager.volverAItinerarioIda.bind(NavigationManager);
        window.enviarDatosPasajero = FormManager.enviarDatosPasajero.bind(FormManager);

        // Función global para limpiar manualmente (útil para testing)
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
        FormValidationManager.init(); // ✅ NUEVO: Inicializar validación en tiempo real

        // Inicializar sistema de pago cuando llegue al paso 3
        this.inicializarPagoCondicional();
    },

    inicializarPagoCondicional() {
        // Si ya estamos en el paso de pago, inicializar inmediatamente
        if (AppState.currentStep === 3) {
            PaymentManager.initialize();
        }

        // También observar cambios de paso para inicializar cuando sea necesario
        const originalSetCurrentStep = AppState.setCurrentStep;
        AppState.setCurrentStep = function (step) {
            originalSetCurrentStep.call(this, step);
            if (step === 3) {
                // Pequeño delay para asegurar que el DOM esté listo
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

// =============================================================================
// EXPORTACIONES (si es necesario para módulos)
// =============================================================================

// Si necesitas usar estos como módulos ES6, puedes exportar:
/*
export {
    CONFIG,
    AppState,
    Venta,
    NavigationManager,
    SearchManager,
    RouteManager,
    ItineraryManager,
    VehicleLayoutManager,
    SeatManager,
    FormManager,
    PaymentManager,
    ReniecAPI,
    TimerManager,
    App
};
*/