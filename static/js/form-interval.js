/* показывать всплываеющее окно с периодичностью */
/* не показывать на странице бронирования */
if (!(document.getElementsByClassName("no-modal")[0])) {
    setInterval (function() {
        document.getElementById("popup-form").style.display = "flex";
        },
        10000);
}



/* закрыть всплывающее окно */
el_close = document.getElementById('popup-close')
el_close.addEventListener(
    "click",
    function(event){
        document.getElementById("popup-form").style.display = "none";
    })


/* закрыть всплывающее окно при бронировании*/
el_booking = document.getElementById('popup-booking')
el_booking.addEventListener(
    "click",
    function(event){
        modal = document.getElementById("popup-form");
        modal.style.display = "none";
    })




