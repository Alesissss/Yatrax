export function buscarPersona(asiento) {
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