var fac = function(n){
    if (n===0) return 1;
    return n * fac(n - 1);
};

var memoFac = (function () {
    var cache = {};
    return function (x) {
        if (!(x in cache)) {
            console.log('mise en cache de fac(' + x + ')');
            cache[x] = fac(x);
        }
        return cache[x];
    };
}());

var memofac = (function (){
    var cache = {};
    return function(n) {
        var value;
        if (!(n in cache)) {
            console.log("mise en cache de (" + n + ")");
            if (n === 0) {
                value = 1;
            } else {
                value = n * memofac(n - 1);
            }
            cache[n] = value;
        }
        return cache[n];
    }                
})();


var fibo = function(n){
    if (n===0) return 0;
    if (n===1) return 1;
    return fibo(n-1) + fibo(n-2);
}



var memoFibo = (function () {
    var cache = {};
    return function (x) {
        var value;
        if (!(x in cache)) {
            console.log('mise en cache de fibo(' + x + ')');
            if (x === 0) {
                value = 0;
            }
            else if (x === 1) {
                value = 1;
            }
            else {
                value = memoFibo(x - 1) + memoFibo(x - 2);
            }
            cache[x] = fibo(x);
        }
        return cache[x];
    };
}());






var suite_geo = function(u0,r,n){
    if (n===0) return u0;
    return u0*Math.pow(r,n);
}


var memoSuite_geo = (function () {
    var cache = {};
    return function (u0,r,n) {
        var value;
        if (!(n in cache)) {
            if (n === 0) {
                value = u0;
            }
            else {
                value = u0*Math.pow(r,n);
            }
            cache[n] = value;
        }
        return cache[n];
    }})();