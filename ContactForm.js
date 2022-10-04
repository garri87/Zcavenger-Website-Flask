




function submitForm(){


    const formName = document.getElementById('formName').value
    const formMail = document.getElementById('formMail').value
    const formMessage = document.getElementById('formMessage').value

    const submitButton = document.getElementById('submit')
    if (formName.length && formMail.length > 0) 
    {
        alert("Thank you, " + formName + " your message was received correctly")
    }

}