
pieces = document.querySelectorAll('.piece')
piece_forms = document.querySelectorAll('.form-piece')

pieces.forEach(p => {
    // console.log(p)
    piece_forms.forEach(f => {
        // console.log(f)
        if (p.getAttribute('id_value') == f.getAttribute('id_value')){
            // console.log('id_value ' + p.getAttribute('id_value') + ' - ' + f.getAttribute('id_value'))
            // console.log('id ' + p.id + ' - ' + f.id)

            //console.log(p.getElementsByClassName('piece_body')[0].textContent)
            f.getElementsByClassName('piece_name_input')[0].setAttribute(
                'value',
                p.getElementsByClassName('piece_name')[0].textContent
            )

            //console.log(p.getElementsByClassName('is_secret')[0].getAttribute('value') == 'False' ? false : true)
            // f.getElementsByClassName('is_secret_input')[0].setAttribute(
            //     'value',
            //     p.getElementsByClassName('is_secret')[0].getAttribute('value') == 'True' ? 'True' : 'False'
            // )
            if (p.getElementsByClassName('is_secret')[0].getAttribute('value') == 'True') f.getElementsByClassName('is_secret_input')[0].checked = true
            else f.getElementsByClassName('is_secret_input')[0].checked = false

            //console.log(p.getElementsByClassName('piece_body').textContent)
            f.getElementsByClassName('body_input')[0].innerHTML = p.getElementsByClassName('piece_body')[0].textContent
            f.getElementsByClassName('body_input')[0].setAttribute(
                'value',
                p.getElementsByClassName('piece_body')[0].textContent
            )


            p.getElementsByClassName("btn-info")[0].onclick = () => { 
                // console.log(f)
                f.classList.toggle('d-block')
                f.classList.toggle('d-none')
                p.classList.toggle('d-block')
                p.classList.toggle('d-none')
            };

             f.getElementsByClassName("btn-info")[0].onclick = () => { 
                // console.log(f)
                f.classList.toggle('d-block')
                f.classList.toggle('d-none')
                p.classList.toggle('d-block')
                p.classList.toggle('d-none')
            };
        }
    })
});