function init() {
    $('#tabs').tabs().find(".ui-tabs-nav" ).sortable({ axis: 'x' });
    $('#tabs').tabs({selected: 0});
    
    document.getElementById("tabs").style.visibility="visible";
    
    // init Tabs
    $(function() {
	    $('#tabs').tabs({
		    select :
		    function(event, ui) {
			var tabName = $(ui.tab).text();

                        if(tabName == 'Basic') {
                            document.getElementById("iframe0").src = "/cgi-bin/webinterface0.sh";
                        }
			
                        if(tabName == 'Advanced') {
			    document.getElementById("iframe2").src = "/cgi-bin/webinterface2.sh";
                        }
			
			if(tabName == 'QoS') {
			    document.getElementById("iframe3").src = "/cgi-bin/webinterface3.sh";
                        }

			if(tabName == 'Tracking') {
			    document.getElementById("iframe8").src = "/cgi-bin/flir.sh";
			}

                        if(tabName == 'Serial Port Setup') {
                            document.getElementById("iframe5").src = "/cgi-bin/webinterface5.sh";
			}

                        if(tabName == 'Node Diagnostics') {
                            document.getElementById("iframe6").src = "/cgi-bin/webinterface7.sh";
			}
			
                        if(tabName == 'Build Information') {
                            document.getElementById("iframe7").src = "/cgi-bin/webinterface6.sh";
                        }
			
			if(tabName == 'StreamScape Network Manager') {
			    location.href = "netmgmt_dev.html";
			}
		    }
		});
	    
	    $(window).resize(function() {
		});
	    $(window).unload(function() {  // disable network management/bcast updates
		});
	});
    //check for overheat and shutdown warnings every 10 sec.
    checkWarning();
}


function displayTempLog() {
    //copy the log file to cgi_bin directory from tmp_mnt
    var req = new XMLHttpRequest();
    var d = new Date();

    req.onreadystatechange = function() {
	    if (req.readyState === 4) {  
		    if (req.status === 200) {
			var temp_log_win= window.open("",name="TEMP_LOG");
			//temp_log_win.document.getElementById("tempLog").innerHTML=req.responseText;
			temp_log_win.document.write(req.responseText.replace(/\n/g, "<br/>"));
			temp_log_win.document.close();

			temp_log_win.outerHeight=1200;
			temp_log_win.outerWidth=600;
		    }
	   }
	};
    req.open("GET", "/cgi-bin/copy_temp_log.sh?" + d.getTime(), true);
    req.send();


    
   /* setInterval(function(){
	    temp_log_win.open("temp_log.html",name="TEMP_LOG");
	    temp_log_win.document.getElementById("tempLog").innerHTML=req.responseText
	    temp_log_win.outerHeight=1200;
	    temp_log_win.outerWidth=600;

	    
	},10000);
*/
}

function checkWarning(){
    var overheatFile = new XMLHttpRequest();
    
    overheatFile.onreadystatechange = function() {
	if (overheatFile.readyState === 4) {  
	    if (overheatFile.status === 200) {
		warning = overheatFile.responseText.replace(/\n/g, ""); 
		if(warning=="1") {
		    var warning_win=window.open("WARNING.txt",name="WARNING");
		    warning_win.outerHeight=300;
		    warning_win.outerWidth=600;
		    
		}
		/*if(warning=="0"){
		  if(warning_win){
		  warning_win.open("WARNING.txt",name="WARNING");
		  warning_win.outerHeight=300;
		  warning_win.outerWidth=600;
		  
		  }
		  }*/
	    }
	}
    };
    
    
    setInterval(function() {
	    overheatFile.open("GET", "/cgi-bin/OVERHEAT_WARNING_FLAG.txt", true);
	    overheatFile.send();
	}, 5000);

    var shutdownFile = new XMLHttpRequest();
    
    shutdownFile.onreadystatechange = function() {
	if (shutdownFile.readyState === 4) {  // Makes sure the document is ready to parse.
	    if (shutdownFile.status === 200) {  // Makes sure it's found the file.
		warning = shutdownFile.responseText.replace(/\n/g, ""); 
		if(warning=="1"){
		    alert("Node is shutting down..\n Please close this browser window");
		}
	    }
	}
    };

    setInterval(function() {
	    shutdownFile.open("GET", "/cgi-bin/SHUTDOWN_WARNING_FLAG.txt", true);
	    shutdownFile.send();
	}, 5000);
}
