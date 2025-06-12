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
