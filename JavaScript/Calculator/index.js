let output = document.getElementById('out');
let result='';
 buttons=document.querySelectorAll('button');
 Array.from(buttons).forEach(element=>{

    element.addEventListener('click',(e)=>{
        buttonText=e.target.innerText;
        console.log(buttonText);
    
        if(buttonText=='C'){
            output.value='';
            result='';
            

        }
        else if(buttonText=='='){
            output.value=eval(result);

        

        }
        else{
            result+=buttonText;
            output.value=result;

        }
    })
})

