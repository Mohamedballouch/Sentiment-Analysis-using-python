$("#sub").click(function(event){
event.preventDefault();
         var text1 = $.trim($("#text1").val());
        console.log(text1);

         $.ajax({
            url: "/get_data",
            type: "POST",
            data: {text1: text1},
           success: function(response) {
        console.log(response)
            $("#output").html(`<h2> The sentiment of </h2> <p>${response.text1}</p> <h2> is ${response.final} % positive !</h2> `);
         },
          error: function(xhr) {
        console.log("hey bro :"+xhr)
        }
       });
$("#text1").val("");
     });