/**
 * Función que verifica si el usuario
 * quiere eliminar una pelicula de acuerdo con
 * su id.
 * @param {*} id 
 */
function eliminarPelicula(id) {
    Swal.fire({
        title: "Desea eliminar la pelicula?",
        showDenyButton: true,
        confirmButtonText: "SI",
        denyButtonText: "NO"
    }).then((result) => {
        if (result.isConfirmed) {
            location.href = "/eliminarPelicula/" + id
        }
    });
}

