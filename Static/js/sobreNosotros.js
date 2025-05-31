// window.addEventListener("DOMContentLoaded", () => {
//   $.ajax({
//     url: "/ecommerce/home/GetConfApariencia",
//     type: "GET",
//     dataType: "json",
//     success: function (response) {
//       if (response.Status === "success") {
//         const config = response.data;

//         $("#maestra_header")[0].style.setProperty(
//           "background-color",
//           config.color_header,
//           "important"
//         );
//         $("#maestra_footer")[0].style.setProperty(
//           "background-color",
//           config.color_footer,
//           "important"
//         );

//         $("#maestra_logo").attr("src", config.logo);
//       } else {
//         console.error("Error al obtener la configuración:", response.Msj);
//       }
//     },
//     error: function (xhr, status, error) {
//       console.error("Error en la solicitud AJAX:", error);
//     },
//   });
// });

gsap.registerPlugin(ScrollTrigger);

// Selecciona todas las cards
document
  .querySelectorAll("#ctn_informativo .card")
  .forEach((card, i, cards) => {
    ScrollTrigger.create({
      trigger: card,
      start: "top 12vh", // justo debajo del nav
      end: () => "+=" + window.innerHeight,
      pin: false,
      pinSpacing: false,
      scrub: false,
      markers: false,
      pin: i !== cards.length - 1, // el último no se pinnea
      onEnter: () => card.classList.add("expanded"),
      onEnterBack: () => card.classList.add("expanded"),
      onLeave: () => card.classList.remove("expanded"),
      onLeaveBack: () => card.classList.remove("expanded"),
    });
  });

const section = document.querySelector("#fundadores");

// Calculamos cuánto tenemos que desplazar en X:
// ancho total del contenido menos el ancho de la ventana
const totalScroll = section.scrollWidth - window.innerWidth;

gsap.to(section, {
  x: -totalScroll,
  ease: "none",
  scrollTrigger: {
    trigger: section,
    start: "top top", // cuando el top de #fundadores llegue al top de la ventana
    end: () => "+=" + totalScroll, // la distancia de scroll que activará toda la animación
    scrub: true, // sincroniza el animation con el scroll
    pin: true, // fija la sección en pantalla mientras dura el scroll
    anticipatePin: 1, // inicia el pinning un poco antes
  },
});
