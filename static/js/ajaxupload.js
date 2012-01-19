
jQuery.extend({

    createUploadIframe: function(id, uri){

            var frameId = 'jQuery' + id;

            if(window.ActiveXObject) {
                var io = document.createElement('<iframe id="' + frameId + '" name="' + frameId + '" />');

                if(typeof uri== 'boolean'){
                    io.src = 'javascript:false';
                }
                else if(typeof uri== 'string'){
                    io.src = uri;
                }
            }
            else {
                var io = document.createElement('iframe');
                io.id = frameId;
                io.name = frameId;
            }

            io.style.position = 'absolute';
            io.style.top = '-1000px';
            io.style.left = '-1000px';

            document.body.appendChild(io);

            return io

    },

    ajaxUpload: function(s) {
        // TODO introduce global settings, allowing the client to modify them for all requests, not only timeout
        s = jQuery.extend({}, jQuery.ajaxSettings, s);

        var id = new Date().getTime()
        io = jQuery.createUploadIframe(id, s.secureuri)

        // Watch for a new set of requests
        if ( s.global && ! jQuery.active++ )
            jQuery.event.trigger( "ajaxStart" );

        var requestDone = false;

        // Create the request object
        var xml = {}
        if ( s.global )
            jQuery.event.trigger("ajaxSend", [xml, s]);

        // Wait for a response to come back
        var uploadCallback = function(isTimeout){
            try {
                xml.responseText = io.contentWindow.document.body?io.contentWindow.document.body.innerHTML:null;
                xml.responseXML = io.contentWindow.document.XMLDocument?io.contentWindow.document.XMLDocument:io.contentWindow.document;
            }
            catch(e){}

            if ( xml || isTimeout == "timeout") {
                requestDone = true;
                var status;
                try {
                    status = isTimeout != "timeout" ? "success" : "error";
                    // Make sure that the request was successful or notmodified
                    if ( status != "error" ) {
                        // process the data (runs the xml through httpData regardless of callback)
                        var data = jQuery.uploadHttpData( xml, s.dataType );

                        // If a local callback was specified, fire it and pass it the data
                        if ( s.success )
                            s.success( data, status );

                        // Fire the global callback
                        if( s.global )
                            jQuery.event.trigger( "ajaxSuccess", [xml, s] );
                    } else
                        jQuery.handleError(s, xml, status);
                } catch(e) {
                    status = "error";
                    jQuery.handleError(s, xml, status, e);
                }

                // The request was completed
                if( s.global )
                    jQuery.event.trigger( "ajaxComplete", [xml, s] );

                // Handle the global AJAX counter
                if ( s.global && ! --jQuery.active )
                    jQuery.event.trigger( "ajaxStop" );

                // Process result
                if ( s.complete )
                    s.complete(xml, status);

                jQuery(io).unbind()

                setTimeout(function(){ document.body.removeChild(io); }, 100)

                xml = null

            }
        }
        // Timeout checker
        if ( s.timeout > 0 ) {
            setTimeout(function(){
                // Check to see if the request is still happening
                if( !requestDone ) uploadCallback( "timeout" );
            }, s.timeout);
        }
        try {
            var frameId = 'jQuery' + id;
            var io = document.getElementById(frameId);
            // Initialize the HTML form properties in case they are
            // not defined in the HTML form.
            s.uploadform.action = s.url;
            s.uploadform.method = 'POST';
            s.uploadform.target = frameId;

            if(s.uploadform.encoding){
                // IE does not respect property enctype for HTML forms.
                // Instead use property encoding.
                s.uploadform.encoding = 'multipart/form-data';
            }
            else{
                s.uploadform.enctype = 'multipart/form-data';
            }

            s.uploadform.submit();

        } catch(e) {
            jQuery.handleError(s, xml, null, e);
        }

        if(window.attachEvent){
            io.attachEvent('onload', uploadCallback);
        }
        else{
            io.addEventListener('load', uploadCallback, false);
        }

        return {abort: function () {}};

    },

    uploadHttpData: function( r, type ) {
        var data = !type;
        data = type == "xml" || data ? r.responseXML : r.responseText;

        // If the type is "script", eval it in global context
        if ( type == "script" ) {
            jQuery.globalEval( data );
				}
        // Get the JavaScript object, if JSON is used.
        if ( type == "json" ) {
            eval( "data = " + data );
        }

        // evaluate scripts within html
        if ( type == "html" ) {
            jQuery("<div>").html(data).evalScripts();
        }

        return data;
    }
})

