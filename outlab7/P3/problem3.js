$(document).ready(function(){
    var $results = $('a:contains("Text")').filter(function() {
            return $(this).text() === 'Text';
    });
        $results.next("ul").css({"background-color": "red", "color": "blue"});
        $("ol:first li").append(" in the list!");
        $("a[name]").css("background-color", "#eee");
    var $results2 = $('a:contains("Some link")').filter(function() {
        return $(this).text() === 'Some link';
    });
        $results2.click(function(){
            alert("Some link is clicked");
        });
});

