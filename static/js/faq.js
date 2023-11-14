// обработка после загрузки страницы
window.addEventListener('load', () => {
  //alert('Страница загружена!');

  ul = document.getElementById('faq-list');
  children_div = ul.querySelectorAll('.faq-item');

  for (var i = 0; i < children_div.length; i++){
    children_div[i].hidden = true;
  }
});


// событие на элдемент списка с вопросами
el = document.getElementById('faq-list')
el.addEventListener(
    "click",
    function(event){
        if (event.target.tagName != 'A')
            return;

        let childrenList = event.target.parentNode.querySelector('.faq-item');
        if (!childrenList)
            return;

        childrenList.hidden = !childrenList.hidden;

        if (childrenList.hidden) {
            event.target.classList.add('hide');
            event.target.classList.remove('show');
        }
        else {
            event.target.classList.add('show');
            event.target.classList.remove('hide');
        }

    }
)
