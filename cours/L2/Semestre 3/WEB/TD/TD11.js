
document.addEventListener("DOMContentLoaded", function(){
    var c = document.getElementById('container');
    var d = document.getElementById('log');
    for (var i = 0; i < 10; i++) {
        var b = document.createElement('button')
        b.textContent = "bouton " + i
        b.addEventListener("click", function(v){
            return function(){
                d.textContent = v;
            }
        }(i))
    };
    c.appendChild(b);
});

function main(){
    var c = document.getElementById('container');
    var l = document.getElementById('log');
    for( let i = 0;i<10;i++){
        var b = document.createElement('button');
        b.textContent = i;
        b.addEventListener('click', function(v){
            return function(){
                l.textContent = v;
            }
        }(i)
    )
    setTimeout(function(elm){
        elm.parentNode.removeChild(elm);
    })
    (b), Math.random()*5000 + 5000;
    c.appendChild(b)
}
}