$(document).ready(function(){
    var $results = $('a:contains("Text")').filter(function() {
            return $(this).text() === 'Text';
    });
        $results.next("ul").css({"background-color": "red", "color": "blue"});
        $("ol:first li").append(" in the list!");
        $("body").css("background-color", "#eee");

        $("a").click(function(){
            alert("Some link is clicked");
        });
});

