;(function(){
    var openSidebarE = document.getElementById("open-sidebar");
    var sidebarE = document.getElementById("sidebar");
    openSidebarE.onclick = function(){
        openSidebarE.classList.toggle("open");
        sidebarE.classList.toggle("sidebar-open")
    }
    
    
    
})();