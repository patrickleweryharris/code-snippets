/* Used to create a list of courses for plh.io/major-finder */
var course_list = [];
function get_list(){
  $.getJSON("https://raw.githubusercontent.com/patrickleweryharris/major-finder/master/json/majors.json", function(data){
    for (i = 0; i < data.length; i++){
      course_list = course_list.concat(data[i].requirements);
    }
    var uniqueArray = course_list.filter(function(elem, pos) {
      return course_list.indexOf(elem) == pos;
    });
    console.log(uniqueArray);
    document.getElementById("theOutput").innerHTML = uniqueArray;
  });
}
