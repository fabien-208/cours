
//exercice 1

// question 1

function arithm(r, init = 0){
    return function(n){
        return init + r * n;
    }
}

//question 2

function geo(r, init = 1){
    return function(n){
        return init * Math.pow(r, n);
    }
}


function suite(f, init = 0){
    return function(n){
        let res = init;
        for(let i = 1; i <= n; i++){
            res = f(res, i);
        }
        return function(m){
            return f(res, m);
        }
    }
}

function suite(f, init = 0){
    return function(n){
        let res = init;
        for(let i = 1; i <= n; i++){
            res = f(res, i);
        }
        return res;
    }
}


function main(){
    console.log(arithm(2)(4)); // 8
    console.log(arithm(2, 1)(4)); // 9
    console.log(geo(2, 1)(4)); // 16
    console.log(suite((x, y) => x + y, 0)(2)(4)); // 8 
    console.log(suite((x, y) => x * y, 1)(2)(4)); // 16 
}

main();