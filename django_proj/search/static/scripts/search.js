$(document).ready(function() 
    { 
        //$("#results-table").tablesorter(); 
        $("#results-table").DataTable({
          paging: false
        }); 
        
        $(".shrink-div form").toggle();
        $(".shrink-div .head-div").toggleClass("padding-expand");
        
        $(".shrink-div .head-div").click(function() {
            console.log("HEAD DIV CLICKED");
            $(".shrink-div form").toggle(200);
            $(".shrink-div .head-div").toggleClass("padding-expand");
            });
    } 
);