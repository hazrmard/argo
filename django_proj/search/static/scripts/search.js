$(document).ready(function() 
    { 
        //$("#results-table").tablesorter(); 
        $("#results-table").DataTable({
          paging: false
        }); 
        $(".shrink-div form").toggle();
        $(".shrink-div").toggleClass("padding-expand");
        $(".shrink-div").click(function() {
            $(".shrink-div form").toggle(200);
            $(".shrink-div").toggleClass("padding-expand");
            });
    } 
);