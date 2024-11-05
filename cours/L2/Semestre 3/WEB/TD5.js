// question 1

function premier_noeud(n) {
    n=n.firstChild;
    var m;
    while (n) {
        if (n.nodeType == node.element_node && n.nodeName == 'p') {
            return n;
        } else{
            m = premier_noeud(n);
            if (m !== null) {
                return m;
            }
        }
        n = n.nextSibling;
    }
    return null;
}
    
// question 2


function majuscule(n){
    if(n.nodeType == Node.TEXT_NODE){
        n.nodeValue = n.nodeValue.toUpperCase();
    }
    for (var i = 0; i < n.childNodes.length; i++) {
        majuscule(n.childNodes[i]);
    }
    return;
}


// question 3

function majuscule_H1(n){
    if(n.nodeType == Node.TEXT_NODE){
        n.nodeValue = n.nodeValue.toUpperCase();
    }
    for (var i = 0; i < n.childNodes.length; i++) {
        if (n.childNodes[i].nodeName == 'H1') {
            majuscule(n.childNodes[i]);
        }
    }
}