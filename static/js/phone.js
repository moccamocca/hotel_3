/* в поле с номером телефона можно вводить только цифры  */
function changeSumv(e) {
    var val = this.value;
    if (val != ''){
        this.value = val.replace(/[A-Za-zА-Яа-яЁё !@#$%^&*_,.?;:№/{}|><=\''""]/g, '');
    } else {
        this.value = ''
    }

};

"input change paste".split(" ").forEach(function(e){
      id_phone.addEventListener(e, changeSumv, false);
    });


/* маска для ввода номера телефона */
document.addEventListener('DOMContentLoaded', () => {

    const inputElement = document.querySelector('[data-mask="phone"]')

    const maskOptions = { // создаем объект параметров
        mask: '+{7}(000)000-00-00' // задаем единственный параметр mask
    }

  IMask(inputElement, maskOptions) // запускаем плагин с переданными параметрами

})
