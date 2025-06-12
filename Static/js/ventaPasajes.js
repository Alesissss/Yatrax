let currentStep = 0;
let maxStep = 0; // Controla hasta qué pestaña está desbloqueado el acceso

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

    if (!itinerarios || itinerarios.length === 0) {
        contenedor.innerHTML = '<p class="text-center">No hay itinerarios disponibles.</p>';
        return;
    }

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

    //Api RENIEC
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

    //Fin api reniec

}

function generarMatriz(id_boton, piso) {
    let botones_guardados
    ruta = "/ecommerce/home/obtener_diseno_vehiculo"
    enviar = { "id_dv": id_boton }
    fetch(ruta, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(enviar)
    })
        .then(res => res.json())
        .then(res => {
            botones_guardados = res.data
            const filas = 15;
            const columnas = 6;
            console.log(`matrizContainer_${piso}`)
            const contenedor = document.getElementById(`matrizContainer_${piso}`);

            if (!contenedor || contenedor.children.length > 0) return;

            contenedor.innerHTML = '';

            // Estilos de grilla
            contenedor.style.display = 'grid';
            contenedor.style.gridTemplateColumns = `repeat(${columnas}, 40px)`;
            contenedor.style.gridTemplateRows = `repeat(${filas}, 40px)`;
            contenedor.style.gap = '2px';
            contenedor.style.justifyContent = 'center';

            for (let i = 1; i <= filas; i++) {
                for (let j = 1; j <= columnas; j++) {
                    const btn = document.createElement('button');
                    btn.className = 'btn btn-light border-dark';
                    btn.style.width = '40px';
                    btn.style.height = '40px';
                    btn.setAttribute('data-x', j);
                    btn.setAttribute('data-y', i);
                    btn.setAttribute('data-tipo', '');

                    // Verifica si hay herramienta en esta posición
                    const boton_existente = botones_guardados.find(b =>
                        parseInt(b.x_dimension) === j &&
                        parseInt(b.y_dimension) === i &&
                        parseInt(b.piso) === piso
                    );

                    if (boton_existente) {
                        const iconoHTML = obtenerIcono(boton_existente.id_herramienta);
                        btn.innerHTML = iconoHTML;
                        btn.setAttribute('data-tipo', boton_existente.id_herramienta);
                    }

                    contenedor.appendChild(btn);
                }
            }
        });




}

const list_herramientas = JSON.parse('{{ herramientas | tojson }}');

function obtenerIcono(idHerramienta) {
    const herramienta_dict = list_herramientas.find(h => h.id === parseInt(idHerramienta));
    if (herramienta_dict) {
        return `<i class="${herramienta_dict.icono}"></i>`
    }
    return '';
}









