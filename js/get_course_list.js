/* Used to create a list of courses for plh.io/major-finder */
var course_list = ["ANT100","ANT200","ANT207","BIO120","BIO130","BIO150","BIO220","CHM135","CHM136","CHM138","CHM139","CHM151","CIN105","CLA160","CSC104","CSC108","CSC120","CSC121","CSC148","CSC165","CSC240","EAS103","EAS105","ECO100","ECO105","ENG110","ENG140","ENG150","EST100","EST101","FAH102","FIN100","FIN110","FSL100","FSL102","FSL121","FSL221","GER100","GGR100","GGR101","GGR107","GGR112","GGR124","GGR270","HIS100","HIS101","HIS102","HIS103","HIS106","HIS107","HIS109","HMU111","HMU126","HPS100","HPS110","HPS120","HUN100","ITA100","JAV120","JAV130","JEG100","JMB170","LIN100","LIN102","MAT133","MAT135","MAT136","MAT137","MAT157","MAT223","MAT224","MAT240","MAT247","MGR100","MGR101","MSE101","MUS110","MUS111","NEW120","NEW150","PHL100","PHL232","PHL233","PHY131","PHY132","PHY151","PHY152","POL101","POl101","PRT100","PRT120","PSL190","PSY100","RLG100","RLG101","RSM100","SAS114","SLA100","SLA101","SLA105","SLA106","SLA108","SLA109","SLA204","SLA208","SLA220","SMC103","SMC141","SMC175","SMC176","SMC188","SOC101","SOC102","SOC103","SPA100","TMU115","TMU140","TRN150","TRN151","USA200","VIC202","VIS120","VIS130","WGS160"];
function get_list(){
  $.getJSON("https://raw.githubusercontent.com/patrickleweryharris/major-finder/master/json/utm.json", function(data){
    for (i = 0; i < data.length; i++){
      course_list = course_list.concat(data[i].requirements);
    }
    console.log(course_list);
    var uniqueArray = course_list.filter(function(elem, pos) {
      return course_list.indexOf(elem) == pos;
    });
    console.log(uniqueArray);
    document.getElementById("theOutput").innerHTML = uniqueArray;
  });
}
