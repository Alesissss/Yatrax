let currentStep = 0;
let maxStep = 0; // Controla hasta qué pestaña está desbloqueado el acceso
const MAX_ASIENTOS = 4;

function updateFormVisibility() {
    const form = document.getElementById('form-destino');
    const steps = document.querySelectorAll('.step');
    const tabs = document.querySelectorAll('.tab-link');

    form.classList.toggle('hidden', currentStep === 3);

    steps.forEach(step => step.classList.remove('active'));
    tabs.forEach(tab => tab.classList.remove('active', 'disabled'));

    steps[currentStep].classList.add('active');
    tabs[currentStep].classList.add('active');

    tabs.forEach((tab, index) => {
        if (index > maxStep) {
            tab.classList.add('disabled');
            tab.setAttribute('disabled', 'true');
        } else {
            tab.removeAttribute('disabled');
        }
    });
}

function buscarYMostrarItinerario() {
    const ruta = $('#cbx_Ciudades').val();
    const ida = $('input[name="fecha_ida"]').val();

    if (!ruta || !ida) {
        toastr.warning("Debes completar origen, destino y fecha de ida.");
        return;
    }

    if (currentStep > 0) {
        Swal.fire({
            title: "¿Realizar nueva búsqueda?",
            text: "Realizar una nueva búsqueda eliminará tu progreso actual, ¿estás seguro?",
            icon: "warning",
            showCancelButton: true,
            confirmButtonText: "Sí, buscar",
            cancelButtonText: "Cancelar"
        }).then((result) => {
            if (result.isConfirmed) {
                ejecutarBusqueda();
            }
        });
    } else {
        ejecutarBusqueda();
    }
}

function ejecutarBusqueda() {
    const datos = capturarDatos();

    $.ajax({
        url: '/ecommerce/home/buscarViajes',
        data: datos,
        method: 'POST',
        success: function (resp) {
            if (resp.Status == 'success') {
                if (!resp.data_ida || resp.data_ida.length === 0) {
                    toastr.warning("No se han encontrado viajes para esas fechas");
                    return;
                }
                cargarItinerario(resp.data_ida, 'contenedor_viajes_ida');
                currentStep = 1;
                maxStep = 1; // Reinicia el máximo al tab 1 tras una nueva búsqueda
                updateFormVisibility();
                toastr.success('VIAJES RETORNADOS CORRECTAMENTE');
            } else {
                toastr.warning('ERROR AL BUSCAR EL VIAJE: ' + resp.Msj);
            }
        },
        error: function () {
            toastr.error("Error en la conexión al servidor.");
        }
    });
}

function formatearFechas() {
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

function fct_CargarRutas() {
    $.getJSON('/ecommerce/home/GetRutasConcatenadas', function (response) {
        if (response.Status === 'success') {
            const items = response.data.map((item, index) => ({
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
        } else {
            $('#cbx_Ciudades').html('<option disabled>-- No hay rutas disponibles --</option>').select2({
                width: '100%',
                theme: 'bootstrap4',
                minimumResultsForSearch: Infinity,
                allowClear: false
            });
        }
    });
}

function capturarDatos() {
    const texto = $('#cbx_Ciudades').select2('data')[0].text.split(' - ');
    return {
        origen: texto[0],
        destino: texto[1],
        fecha_ida: $("input[name='fecha_ida']").val(),
        fecha_vuelta: $("input[name='fecha_vuelta']").val()
    };
}

// Eventos en botones Siguiente de cada step
$(document).on('click', '.btn-siguiente', function () {
    if (currentStep < 3) {
        currentStep++;
        if (currentStep > maxStep) maxStep = currentStep; // Desbloquea siguiente tab
        updateFormVisibility();
    }
});

// Inicialización de pestañas (Tabs bloqueados inicialmente)
document.addEventListener('DOMContentLoaded', function () {
    document.querySelectorAll('.tab-link').forEach(tab => {
        tab.addEventListener('click', (event) => {
            const stepIndex = parseInt(tab.getAttribute('data-step'));
            if (stepIndex <= maxStep) {
                currentStep = stepIndex;
                updateFormVisibility();
            } else {
                event.preventDefault();
                toastr.warning("Debes completar los pasos anteriores para continuar.");
            }
        });
    });

    fct_CargarRutas();
    updateFormVisibility();
    formatearFechas();
});


function cargarItinerario(itinerarios, contenedorId) {
    const contenedor = document.getElementById(contenedorId);
    contenedor.innerHTML = ''; // Limpia

    fetch('/ecommerce/home/renderizar_itinerario', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ itinerarios })
    })
        .then(res => {
            return res.json();  // <- solo si estás 100% seguro de que recibes JSON
        })
        .then(data => {
            document.getElementById("contenedor_viajes_ida").innerHTML = data.html;
            inicializarEventosPostRender();
        })
        .catch(err => {
            toastr.error("Error al renderizar el itinerario: " + (err.message || err));
        });

}


function inicializarEventosPostRender() {
    api_reniec();
    funcionalidadElegir();
}

function funcionalidadElegir() {
    document.querySelectorAll(".mostrarContenido").forEach(btn => {
        btn.addEventListener('click', function () {
            generar_matrices(btn.id)

        });

        const targetId = btn.getAttribute('data-bs-target');
        const target = document.querySelector(targetId);

        if (target) {
            target.addEventListener('shown.bs.collapse', function () {
                seleccionarAsiento();
                iniciarTemporizador(300);
            });
        }

    })

}

function seleccionarAsiento() {
    const asientos = document.querySelectorAll('[data-tipo="1"]');
    if (asientos.length === 0) {
        console.warn("No se encontraron asientos con data-tipo='1'");
    }
    asientos.forEach(btn => {

        btn.addEventListener('click', async function () {
            const contenedor = document.getElementById("contenido_datos");
            const accordion = document.getElementById("accordionPasajeros");
            const nombreAsiento = btn.innerText.trim();
            const accordionItemId = `collapse-${btn.id}`;

            // Si ya estaba seleccionado (intenta deseleccionar)
            if (btn.classList.contains("asiento-seleccionado")) {
                const confirm = await Swal.fire({
                    title: '¿Deseas quitar este asiento?',
                    text: `Se eliminarán los datos ingresados para el asiento ${nombreAsiento}.`,
                    icon: 'warning',
                    showCancelButton: true,
                    confirmButtonText: 'Sí, eliminar',
                    cancelButtonText: 'Cancelar',
                });

                if (confirm.isConfirmed) {
                    btn.classList.remove("asiento-seleccionado");

                    const accordionItem = document.getElementById(accordionItemId)?.closest(".accordion-item");
                    if (accordionItem) accordionItem.remove();

                    // Si no queda ningún asiento, ocultamos todo
                    if (accordion.children.length === 0) {
                        contenedor.classList.add("d-none");
                    }
                }

                return; // no continuar
            }

            // Verifica si se ha alcanzado el máximo
            const seleccionados = document.querySelectorAll(".asiento-seleccionado");
            if (seleccionados.length >= MAX_ASIENTOS) {
                toastr.warning(`Solo puedes seleccionar hasta ${MAX_ASIENTOS} asientos.`);
                return;
            }

            // Selecciona asiento
            btn.classList.add("asiento-seleccionado");

            // Mostrar contenedor si estaba oculto
            if (contenedor.classList.contains("d-none")) {
                contenedor.classList.remove("d-none");
            }

            // Crear el acordeón si no existe
            if (!document.getElementById(accordionItemId)) {
                const headerId = `heading-${btn.id}`;

                const nuevoForm = document.createElement("div");
                nuevoForm.classList.add("accordion-item");

                nuevoForm.innerHTML = `
                    <h2 class="accordion-header" id="${headerId}">
                        <button class="accordion-button ${accordion.children.length > 0 ? 'collapsed' : ''}" type="button" data-bs-toggle="collapse" data-bs-target="#${accordionItemId}" aria-expanded="true" aria-controls="${accordionItemId}">
                        Asiento ${btn.id}
                        </button>
                    </h2>
                    <div id="${accordionItemId}" class="accordion-collapse collapse ${accordion.children.length === 0 ? 'show' : ''}" aria-labelledby="${headerId}" data-bs-parent="#accordionPasajeros">
                        <div class="accordion-body">
                        ${generarFormularioHTML(nombreAsiento, btn.id)}
                        </div>
                    </div>
                    `;

                accordion.appendChild(nuevoForm);
                accordion.appendChild(nuevoForm);
                api_reniec(btn.id); // <== NUEVA LÍNEA

            }

            funcionalidadBotonAsiento(); // tu lógica personalizada
        });


    });
}

function generarFormularioHTML(asiento_nombre,asiento_id) {
  return `
    <div class="mb-2 fw-bold text-primary">Asiento: ${asiento_nombre} (<span>S/0.00</span>)</div>
    <select class="form-select mb-2" id="tipo_doc_${asiento_id}">
      <option value="DNI">DNI</option>
      <option value="CE">CE</option>
    </select>
    <input class="form-control mb-2" id="numeroDocNuevo_${asiento_id}" placeholder="N° Documento">
    <input class="form-control mb-2" id="nombres_${asiento_id}" placeholder="Nombres">
    <input class="form-control mb-2" id="apellidoPaterno_${asiento_id}" placeholder="Apellido paterno">
    <input class="form-control mb-2" id="apellidoMaterno_${asiento_id}" placeholder="Apellido materno">
    <input class="form-control mb-2" id="fechaNacimientoNuevo_${asiento_id}" type="date" placeholder="Fecha nacimiento">
    <input class="form-control mb-2" id="telefono_${asiento_id}" placeholder="Teléfono">
    <div class="mb-2">
      <label class="me-2">Sexo:</label>
      <input type="radio" class="form-check-input" name="sexo-${asiento_id}" id="sexoMasculino_${asiento_id}"> <label for="sexoMasculino_${asiento_id}" value="M">Masculino</label>
      <input type="radio" class="form-check-input" name="sexo-${asiento_id}" id="sexoFemenino_${asiento_id}"> <label for="sexoFemenino_${asiento_id}" value="F">Femenino</label>
    </div>
    <input class="form-control mb-2" id="correo_${asiento_id}" placeholder="Correo electrónico" type="email">
    <div class="form-check">
      <input class="form-check-input" type="checkbox" id="brazos_${asiento_id}">
      <label class="form-check-label" for="brazos_${asiento_id}">Con menor en brazos</label>
    </div>
    <div class="form-check mb-2">
      <input class="form-check-input" type="checkbox" id="esMenor_${asiento_id}">
      <label class="form-check-label" for="esMenor_${asiento_id}">Es menor de edad</label>
    </div>
    <button class="btn btn-outline-primary w-100" onclick='enviarDatosPasajero("${asiento_nombre}",${asiento_id})'>Guardar datos</button>
  `;
}


/* Hay que ver si trabajamos con ES6 para poder colcoar esta clase en un archivo y solo llamar a la clase desde cada una de las parte e ir editando y asignando el resto de valores del resto de fases para despúes de asignar ya se registre la venta */

class Venta {
  constructor(numDoc, nombres, apellidoPaterno, apellidoMaterno, fechaNacimiento, telefono, recuperarSeleccion, sexo, correo, brazos, esMenor) {
    this.numDoc = numDoc;
    this.nombres = nombres;
    this.apellidoPaterno = apellidoPaterno;
    this.apellidoMaterno = apellidoMaterno;
    this.fechaNacimiento = fechaNacimiento;
    this.telefono = telefono;
    this.recuperarSeleccion = recuperarSeleccion;
    this.sexo = sexo;
    this.correo = correo;
    this.brazos = brazos;
    this.esMenor = esMenor;
  }
}

function enviarDatosPasajero(nombre_asiento, id_asiento) {
    const numDoc = document.getElementById(`numeroDocNuevo_${id_asiento}`);
    const nombres = document.getElementById(`nombres_${id_asiento}`);
    const apellidoPaterno = document.getElementById(`apellidoPaterno_${id_asiento}`);
    const apellidoMaterno = document.getElementById(`apellidoMaterno_${id_asiento}`);
    const fechaNacimiento = document.getElementById(`fechaNacimientoNuevo_${id_asiento}`);
    const telefono = document.getElementById(`telefono_${id_asiento}`);
    const correo = document.getElementById(`correo_${id_asiento}`);
    const brazos = document.getElementById(`brazos_${id_asiento}`).checked;
    const esMenor = document.getElementById(`esMenor_${id_asiento}`).checked;

    const recuperarSeleccion = document.querySelector(`input[name="sexo-${id_asiento}"]:checked`)?.id;
    const sexo = recuperarSeleccion?.includes("Masculino") ? 1 : 0;

    const venta = new Venta(
        numDoc.value,
        nombres.value,
        apellidoPaterno.value,
        apellidoMaterno.value,
        fechaNacimiento.value,
        telefono.value,
        recuperarSeleccion,
        sexo,
        correo.value,
        brazos,
        esMenor
    );

    // Puedes guardar en un arreglo por id_asiento
    const ventasGuardadas = JSON.parse(sessionStorage.getItem("ventas") || "{}");
    ventasGuardadas[id_asiento] = venta;
    sessionStorage.setItem("ventas", JSON.stringify(ventasGuardadas));

    toastr.success(`Datos del asiento ${nombre_asiento} guardados correctamente.`);
}


function handleClick(e) {
    console.log("Hola desde asiento", e.currentTarget);
}


function generar_matrices(id_boton) {
    const ruta = "/ecommerce/home/obtener_diseno_vehiculo";
    const enviar = { id_dv: id_boton };

    fetch(ruta, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(enviar),
    })
        .then(res => res.json())
        .then(res => {
            const datos = res.data;

            const datosPiso1 = datos.filter(d => d.nroPiso == 1);
            const datosPiso2 = datos.filter(d => d.nroPiso == 2);

            generarMatrizDesdeDatos(datosPiso1, 1);

            if (datosPiso2.length > 0) {
                document.getElementById('contenedor_piso_2').style.display = 'block';
                generarMatrizDesdeDatos(datosPiso2, 2);
            } else {
                document.getElementById('contenedor_piso_2').style.display = 'none';
            }
        });
}

function generarMatrizDesdeDatos(datos, piso) {
    const filas = 15;
    const columnas = 6;
    const contenedor = document.getElementById(`matrizContainer_${piso}`);

    if (!contenedor) return;
    contenedor.innerHTML = '';

    contenedor.style.display = 'grid';
    contenedor.style.gridTemplateColumns = `repeat(${columnas}, 40px)`;
    contenedor.style.gridTemplateRows = `repeat(${filas}, 40px)`;
    contenedor.style.padding = '10px';
    contenedor.style.margin = '0 auto';
    contenedor.style.width = 'max-content';
    contenedor.style.justifyContent = 'center';
    contenedor.style.border = "2px solid #000";

    for (let y = 1; y <= filas; y++) {
        for (let x = 1; x <= columnas; x++) {
            const dato = datos.find(d =>
                parseInt(d.x_dimension) === x &&
                parseInt(d.y_dimension) === y
            );

            const btn = document.createElement('button');
            btn.style.width = '40px';
            btn.style.height = '40px';
            btn.setAttribute('data-x', x);
            btn.setAttribute('data-y', y);

            if (dato) {
                btn.id = dato.id_asiento ?? '';
                btn.setAttribute('data-tipo', dato.tipo_herramienta);
                btn.style.cursor = 'pointer';

                if (dato.tipo_herramienta === 1) {
                    // Asiento
                    if (dato.estado === 1) {
                        btn.className = 'border border-dark border-2 bg-white';
                        btn.innerText = dato.nombre;
                    } else {
                        btn.innerHTML = obtenerIcono(dato.icono);
                    }
                } else {
                    // Otra herramienta
                    btn.style.border = 'none';
                    btn.style.background = 'transparent';
                    btn.style.cursor = 'default';
                    btn.disabled = true;
                    btn.innerHTML = obtenerIcono(dato.icono);
                }
            } else {
                btn.style.border = 'none';
                btn.style.background = 'transparent';
                btn.style.cursor = 'default';
                btn.disabled = true;
            }

            contenedor.appendChild(btn);
        }
    }
}

function obtenerIcono(icono) {
    return `<img src="/Static/${icono}" width="32" height="32" style="display: block; margin: auto;" alt="icono">`;
}



//Api RENIEC
/*
function api_reniec() {
    let debounceTimer;

    //Captura el input del NroDocumento
    const docInput = document.getElementById("numeroDocNuevo");
    //Captura el input del tipoDocumento
    const tipoDoc = document.getElementById("tipo_doc");
    //Estos dos datos nos permitirá consultar todo

    //Este input permite validar la fecha de nacimiento (Mayor o menor de edad)
    const fechaNac = document.getElementById("fechaNacimientoNuevo");

    if (docInput) {
        docInput.addEventListener("input", function () {
            clearTimeout(debounceTimer);
            debounceTimer = setTimeout(buscarPersona, 1000);
        });
    }

    if (tipoDoc) {
        tipoDoc.addEventListener("change", buscarPersona);
    }

    if (fechaNac) {
        fechaNac.addEventListener("change", validarEdadNuevoPasajero);
    }
}


//Funcion que llama verdaderamente al API de la reniec
function buscarPersona() {

    //Captura el tipo y el numero de doc para poder usar el API Reniec
    const tipoDocVal = document.getElementById("tipo_doc").value;
    const numDoc = document.getElementById("numeroDocNuevo").value.trim();

    if (!tipoDocVal) {
        toastr.warning("El tipo de documento es obligatorio", "MENSAJE DEL SISTEMA");
        return;
    }

    if (tipoDocVal && (numDoc.length == 8 || numDoc.length == 11)) {
        fetch(`/ecommerce/home/api/get_persona_data?tipoDoc=${encodeURIComponent(tipoDocVal)}&numDoc=${encodeURIComponent(numDoc)}`)
            .then((r) => r.json())
            .then((json) => {
                if (json.Status === "success") {
                    const d = json.data;

                    document.getElementById("nombres").value = d.nombres || d.nombre || "";
                    document.getElementById("apellidoPaterno").value = d.apellidoPaterno || d.ape_paterno || "";
                    document.getElementById("apellidoMaterno").value = d.apellidoMaterno || d.ape_materno || "";
                    document.getElementById("correo").value = d.email || "";
                    document.getElementById("telefono").value = d.telefono || "";

                    if (d.f_nacimiento) {
                        document.getElementById("fechaNacimientoNuevo").value = moment(d.f_nacimiento).format("YYYY-MM-DD");
                        validarEdadNuevoPasajero();
                    } else {
                        document.getElementById("fechaNacimientoNuevo").value = "";
                    }

                    if (d.sexo != null) {
                        document.getElementById("sexoMasculino").checked = d.sexo === 1;
                        document.getElementById("sexoFemenino").checked = d.sexo !== 1;
                    } else {
                        document.getElementById("sexoMasculino").checked = false;
                        document.getElementById("sexoFemenino").checked = false;
                    }
                } else {
                    document.getElementById("nombres").value = "Nombres";
                    document.getElementById("apellidoPaterno").value = "Apellido paterno";
                    document.getElementById("apellidoMaterno").value = "Apellido materno";
                    toastr.error(json.Msj, "ERROR");
                }
            })
            .catch(err => {
                toastr.error("Ocurrió un error: " + (err.message || err));
            });
    }
}

function validarEdadNuevoPasajero() {
    const fechaNacimiento = document.getElementById("fechaNacimientoNuevo").value;
    if (!fechaNacimiento) return;

    const fechaActual = new Date();
    const fechaNac = new Date(fechaNacimiento);
    let edad = fechaActual.getFullYear() - fechaNac.getFullYear();
    const mes = fechaActual.getMonth() - fechaNac.getMonth();

    if (mes < 0 || (mes === 0 && fechaActual.getDate() < fechaNac.getDate())) {
        edad--;
    }

    document.getElementById("esMenor").checked = edad < 18;

    if (edad < 18) {
        toastr.warning("Menores a 18 años necesitan presentar autorización de sus padres o tutores para viajar", "MENSAJE DEL SISTEMA");
    }
}
*/
function api_reniec(asiento) {
    let debounceTimer;
    const docInput = document.getElementById(`numeroDocNuevo_${asiento}`);
    const tipoDoc = document.getElementById(`tipo_doc_${asiento}`);
    const fechaNac = document.getElementById(`fechaNacimientoNuevo_${asiento}`);

    if (docInput) {
        docInput.addEventListener("input", function () {
            clearTimeout(debounceTimer);
            debounceTimer = setTimeout(() => buscarPersona(asiento), 1000);
        });
    }

    if (tipoDoc) {
        tipoDoc.addEventListener("change", () => buscarPersona(asiento));
    }

    if (fechaNac) {
        fechaNac.addEventListener("change", () => validarEdadNuevoPasajero(asiento));
    }
}

function buscarPersona(asiento) {
    const tipoDocVal = document.getElementById(`tipo_doc_${asiento}`).value;
    const numDoc = document.getElementById(`numeroDocNuevo_${asiento}`).value.trim();

    if (!tipoDocVal) {
        toastr.warning("El tipo de documento es obligatorio", "MENSAJE DEL SISTEMA");
        return;
    }

    if (tipoDocVal && (numDoc.length == 8 || numDoc.length == 11)) {
        fetch(`/ecommerce/home/api/get_persona_data?tipoDoc=${encodeURIComponent(tipoDocVal)}&numDoc=${encodeURIComponent(numDoc)}`)
            .then((r) => r.json())
            .then((json) => {
                if (json.Status === "success") {
                    const d = json.data;

                    document.getElementById(`nombres_${asiento}`).value = d.nombres || d.nombre || "";
                    document.getElementById(`apellidoPaterno_${asiento}`).value = d.apellidoPaterno || d.ape_paterno || "";
                    document.getElementById(`apellidoMaterno_${asiento}`).value = d.apellidoMaterno || d.ape_materno || "";
                    document.getElementById(`correo_${asiento}`).value = d.email || "";
                    document.getElementById(`telefono_${asiento}`).value = d.telefono || "";

                    if (d.f_nacimiento) {
                        document.getElementById(`fechaNacimientoNuevo_${asiento}`).value = moment(d.f_nacimiento).format("YYYY-MM-DD");
                        validarEdadNuevoPasajero(asiento);
                    }

                    if (d.sexo != null) {
                        document.getElementById(`sexoMasculino_${asiento}`).checked = d.sexo === 1;
                        document.getElementById(`sexoFemenino_${asiento}`).checked = d.sexo !== 1;
                    }
                } else {
                    document.getElementById(`nombres_${asiento}`).value = "Nombres";
                    document.getElementById(`apellidoPaterno_${asiento}`).value = "Apellido paterno";
                    document.getElementById(`apellidoMaterno_${asiento}`).value = "Apellido materno";
                    toastr.error(json.Msj, "ERROR");
                }
            })
            .catch(err => {
                toastr.error("Ocurrió un error: " + (err.message || err));
            });
    }
}



function validarEdadNuevoPasajero() {
    const fechaNacimiento = document.getElementById("fechaNacimientoNuevo").value;
    if (!fechaNacimiento) return;

    const fechaActual = new Date();
    const fechaNac = new Date(fechaNacimiento);
    let edad = fechaActual.getFullYear() - fechaNac.getFullYear();
    const mes = fechaActual.getMonth() - fechaNac.getMonth();

    if (mes < 0 || (mes === 0 && fechaActual.getDate() < fechaNac.getDate())) {
        edad--;
    }

    document.getElementById("esMenor").checked = edad < 18;

    if (edad < 18) {
        toastr.warning("Menores a 18 años necesitan presentar autorización de sus padres o tutores para viajar", "MENSAJE DEL SISTEMA");
    }
}

//Fin api reniec

function iniciarTemporizador(segundos) {
    const elemento = document.getElementById('temporizador');
    let tiempoRestante = segundos;

    const intervalo = setInterval(() => {
        // Calcula minutos y segundos
        const minutos = Math.floor(tiempoRestante / 60);
        const segundosRestantes = tiempoRestante % 60;

        // Formatea con dos dígitos
        const formatoTiempo = `${minutos.toString().padStart(2, '0')}:${segundosRestantes.toString().padStart(2, '0')}`;
        elemento.textContent = `Tiempo restante: ${formatoTiempo}`;

        tiempoRestante--;

        if (tiempoRestante < 0) {
            clearInterval(intervalo);
            elemento.textContent = "¡Tiempo agotado!";
            // Aquí puedes ocultar botones, desactivar funciones, etc.
        }
    }, 1000); // Cada 1 segundo
}

function funcionalidadBotonAsiento(btn_id) {
    const container = document.getElementById("contenido_datos");
    container.classList.remove("d-none");
}




