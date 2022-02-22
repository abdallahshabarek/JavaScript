from string import Template

def render_ui_3d(hexid = 10, analysis_type= "destination", year = "2019", month = "1", resolution = "6", region = "16"):
    results = str("https://raw.githubusercontent.com/abdallahshabarek/JavaScript/main/Dest_Origin/HEXGrid/"+str(year)+"/R"+str(region)+"/M"+str(month)+"/res"+str(resolution)+"/R"+str(region)+"_"+str(analysis_type)+"_"+str(hexid)+"_year"+str(year)+"_M"+str(month)+"_res"+str(resolution)+".geojson")
    print(results)
    html_code =''''
    <!DOCTYPE html>
<html>
<head>
    <!--- https://maptalks.org/maptalks.three/demo/extrudepolygon-china.html--->
    <title>3D Results</title>
    <script type="text/javascript" src="https://unpkg.com/randomcolor@0.6.2/randomColor.js"></script>
    <script type="text/javascript" src="https://unpkg.com/dat.gui@0.7.6/build/dat.gui.min.js"></script>
    <link type="text/css" rel="stylesheet" href="https://unpkg.com/maptalks/dist/maptalks.css">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/maptalks/dist/maptalks.css">
    <script type="text/javascript" src="https://cdn.jsdelivr.net/npm/maptalks/dist/maptalks.min.js"></script>
    <script type="text/javascript" src="https://unpkg.com/three@0.104.0/build/three.min.js"></script>
    <script type="text/javascript"
        src="https://unpkg.com/maptalks.three@latest/dist/maptalks.three.js"></script>
    <style>
        html,
        body {
            margin: 0px;
            height: 100%;
            width: 100%;
        }

        #map {
            width: 100%;
            height: 100%;
            background-color: #000;
        }
    </style>
</head>

<body>
    <div id="map"></div>
    <script>

        var map = new maptalks.Map("map", {
            "center": [-74.169292,40.733648], "zoom": 5.717254596370028, "pitch": 58.40000000000007, "bearing": 0.8533528124999066,

            centerCross: true,
            doubleClickZoom: false,
            baseLayer: new maptalks.TileLayer('tile', {
                urlTemplate: 'https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}.png',
                subdomains: ['a', 'b', 'c', 'd'],
                attribution: '&copy; <a href="http://osm.org">OpenStreetMap</a> contributors, &copy; <a href="https://carto.com/">CARTO</a>'
            })
        });
        // the ThreeLayer to draw buildings
        var threeLayer = new maptalks.ThreeLayer('t', {
            forceRenderOnMoving: true,
            forceRenderOnRotating: true,
            animation: true
        });

        var meshs = [];
        var material = new THREE.MeshBasicMaterial({ color: '#3e35cf', transparent: true, opacity: 0.3 });
        threeLayer.prepareToDraw = function (gl, scene, camera) {
            var light = new THREE.DirectionalLight(0xffffff);
            light.position.set(0, -10, 10).normalize();
            scene.add(light);
            fetch('$url').then(res => res.json()).then(geojson => {
                const time = 'time';
                console.time(time);
                geojson.features.forEach(f => {
                    const m = material.clone();
                    // m.color.setStyle(randomColor());
                    // m.color.setStyle(#fff);
                    const mesh = threeLayer.toExtrudePolygon(f, {
                        height: f.properties.frequency || 10,
                        topColor: '#fff',
                        asynchronous: true
                    }, m);
                    meshs.push(mesh);
                });
                console.timeEnd(time);
                threeLayer.addMesh(meshs);
            })

            threeLayer.config('animation', true);
        };
        threeLayer.addTo(map);


    </script>
</body>
</html>'''
    s = Template(html_code).safe_substitute(url=results)
    return s

def render_ui(hexid = 10, analysis_type = "destination",year = "2019", month = "1", resolution = "6", region ="16"):
    results = str("https://raw.githubusercontent.com/abdallahshabarek/JavaScript/main/Dest_Origin/HEXGrid/"+str(year)+"/R"+str(region)+"/M"+str(month)+"/res"+str(resolution)+"/R"+str(region)+"_"+str(analysis_type)+"_"+str(hexid)+"_year"+str(year)+"_M"+str(month)+"_res"+str(resolution)+".geojson")
    print(results)
    html_code = '''
                <!--- https://www.youtube.com/watch?v=wVnimcQsuwk -->
        <!--- https://cloud.maptiler.com/maps/ --->
        <!--- ladarrius1@netscapezs.com --->
        <!--- https://stackoverflow.com/questions/48202737/data-passing-from-html-text-input-to-python-script --->
        <!--- https://stackoverflow.com/questions/15965646/posting-html-form-values-to-python-script-->

        <!DOCTYPE html>
        <html>
            <head>
                <meta content="text/html;charset=utf-8" http-equiv="Content-Type">
                <meta content="utf-8" http-equiv="encoding">    
                <link rel="stylesheet" href="https://unpkg.com/leaflet@1.7.1/dist/leaflet.css" integrity="sha512-xodZBNTC5n17Xt2atTPuE1HxjVMSvLVW9ocqUKLsCC5CXdbqCmblAshOMAS6/keqq/sMZMZ19scR4PsZChSR7A==" crossorigin="" />
                <script src="https://unpkg.com/leaflet@1.7.1/dist/leaflet.js" integrity="sha512-XQoYMqMTK8LvdxXYG3nZ448hOEQiglfqkJs1NOQV44cWnUrBc8PkAOcXy20w0vlaXaVUearIOBhiXZ5V3ynxwA==" crossorigin=""></script>
                <!-- <script src="https://cdn.jsdeliver.net/npm/promise-polyfill@8/dist/polyfill.min.js"></script> -->
                <script src="https://cdn.jsdelivr.net/npm/whatwg-fetch@2.0.4/fetch.js"></script>
                <style>
                    #map {position: absolute; top:0; bottom:0; left:0; right:0;}
                </style>
                <script
                src="https://code.jquery.com/jquery-3.6.0.min.js"
                integrity="sha256-/xUj+3OJU5yExlq6GSYGSHk7tPXikynS7ogEvDej/m4="
                crossorigin="anonymous"></script>
            </head>



        <body>
            <div id = "map"></div>
            <script>
                var map = L.map('map').setView([40.733648, -74.169292],12);
                L.tileLayer('https://api.maptiler.com/maps/streets/{z}/{x}/{y}.png?key=H1VvbDqGlXLSejjna9W9',{
                    attribution: '<a href="https://www.maptiler.com/copyright/" target="_blank">&copy; MapTiler</a> <a href="https://www.openstreetmap.org/copyright" target="_blank">&copy; OpenStreetMap contributors</a>',
                }).addTo(map);

                L.control.scale({
                    metric: true,
                    imperial: true,
                    position: 'bottomright'
                }).addTo(map);

                L.Control.Watermark = L.Control.extend({
                    onAdd:function(map){
                        var img = L.DomUtil.create('img');
                        img.src = 'https://www.worldhighways.com/sites/ropl-wh/files/2021-03/Bentley-Systems.jpg';
                        img.style.width = '200px'; 
                        return img;
                    },
                    onRemove:function(map){},
                });

                L.control.watermark = function(opts){
                    return new L.Control.Watermark(opts);
                }

                L.control.watermark({position:'bottomleft'}).addTo(map);


                // https://groups.google.com/g/leaflet-js/c/DD2G8jENvFU?pli=1
                

                var myStyle = {
                    "color": "#ff7800",
                    "weight": 5,
                    "opacity": 0.65
                };

                function onEachFeature(feature, layer) {
                    if (feature.properties && feature.properties.hexid_origin) {
                        layer.bindPopup("ID: "+feature.properties.hexid_origin +" freuency: " + feature.properties.frequency);
                    }
                }
                
                function getColor(x) {
                    return x < 50        ?    '#ffffb2':
                            x < 100     ?   '#fecc5c':
                            x < 200     ?   '#fd8d3c':
                            x < 500     ?   '#f03b20':
                                             '#bd0026' ;
                };
                
                // https://gis.stackexchange.com/questions/330443/loading-geojson-file-into-map-in-leaflet
                fetch('$url')
                // fetch("http://localhost:8000/sample.geojson")
                    .then(response => response.json())
                    .then(json => {
                        kaoDist = L.geoJSON(json,
                        {style: function (feature) {
                            return {
                                "color": getColor(feature.properties.frequency),
                                "opacity": 0.5,
                                }
                                }
                        ,onEachFeature: onEachFeature,
                        }
                        ).addTo(map);
                        // kaoDist.bindPopup('<h1>'+feature.properties.frequency); 
                        map.fitBounds(kaoDist.getBounds());
                    });
            </script>
        </body>
        </html>
    '''
    
    s = Template(html_code).safe_substitute(url=results)
    # print(s)
    return s


def render_original():


    
    html_code = '''
        <!--- https://www.youtube.com/watch?v=wVnimcQsuwk -->
        <!--- https://cloud.maptiler.com/maps/ --->
        <!--- ladarrius1@netscapezs.com --->
        <!--- https://stackoverflow.com/questions/48202737/data-passing-from-html-text-input-to-python-script --->
        <!--- https://stackoverflow.com/questions/15965646/posting-html-form-values-to-python-script-->

        <!DOCTYPE html>
        <html>
            <head>
                <meta content="text/html;charset=utf-8" http-equiv="Content-Type">
                <meta content="utf-8" http-equiv="encoding">    
                <!-- <link rel="stylesheet" href="leaflet.css" /> -->
                <link rel="stylesheet" href="https://unpkg.com/leaflet@1.7.1/dist/leaflet.css" integrity="sha512-xodZBNTC5n17Xt2atTPuE1HxjVMSvLVW9ocqUKLsCC5CXdbqCmblAshOMAS6/keqq/sMZMZ19scR4PsZChSR7A==" crossorigin="" />
                <script src="https://unpkg.com/leaflet@1.7.1/dist/leaflet.js" integrity="sha512-XQoYMqMTK8LvdxXYG3nZ448hOEQiglfqkJs1NOQV44cWnUrBc8PkAOcXy20w0vlaXaVUearIOBhiXZ5V3ynxwA==" crossorigin=""></script>
                <!-- <script src="leaflet.js"></script> -->
                <!-- <script src="https://cdn.jsdeliver.net/npm/promise-polyfill@8/dist/polyfill.min.js"></script> -->
                <script src="https://cdn.jsdelivr.net/npm/whatwg-fetch@2.0.4/fetch.js"></script>
                <style>
                    #map {position: absolute; top:0; bottom:0; left:0; right:0;}
                </style>
                <script
                src="https://code.jquery.com/jquery-3.6.0.min.js"
                integrity="sha256-/xUj+3OJU5yExlq6GSYGSHk7tPXikynS7ogEvDej/m4="
                crossorigin="anonymous"></script>
            </head>



        <body>
            <div id = "map"></div>
            <script>
                var map = L.map('map').setView([40.733648, -74.169292],12);
                L.tileLayer('https://api.maptiler.com/maps/streets/{z}/{x}/{y}.png?key=H1VvbDqGlXLSejjna9W9',{
                    attribution: '<a href="https://www.maptiler.com/copyright/" target="_blank">&copy; MapTiler</a> <a href="https://www.openstreetmap.org/copyright" target="_blank">&copy; OpenStreetMap contributors</a>',
                }).addTo(map);

                L.control.scale({
                    metric: true,
                    imperial: true,
                    position: 'bottomright'
                }).addTo(map);

                L.Control.Watermark = L.Control.extend({
                    onAdd:function(map){
                        var img = L.DomUtil.create('img');
                        img.src = 'https://www.worldhighways.com/sites/ropl-wh/files/2021-03/Bentley-Systems.jpg';
                        img.style.width = '200px'; 
                        return img;
                    },
                    onRemove:function(map){},
                });

                L.control.watermark = function(opts){
                    return new L.Control.Watermark(opts);
                }

                L.control.watermark({position:'bottomleft'}).addTo(map);


                // https://groups.google.com/g/leaflet-js/c/DD2G8jENvFU?pli=1
                //Create control
                myControl = L.control({position: 'topleft'});
                myControl.onAdd = function(map) {
                            this._div = L.DomUtil.create('div', 'myControl');
                            this._div.innerHTML =
                            // '<form action="" method = "post"> <p> {{form.hexid.label}} <br> {{form.hexid(size = 30)}} </p> <p> {{form.submit()}} </p> </form>'+
                                                '<form name="region" action="http://localhost:5000/" method="post">'+
                                                'Region: <input name="region" type="text" value="16" />' +
                                                '<form name="year" action="http://localhost:5000/" method="post">'+
                                                'Year: <input name="year" type="text" value="2019" />' +
                                                '<form name="month" action="http://localhost:5000/" method="post">'+
                                                'Month: <input name="month" type="text" value="1" />' +
                                                '<form name="resolution" action="http://localhost:5000/" method="post">'+
                                                'Resolution <input name="resolution" type="text" value="6" />' +
                                                '<form name="analysistype" action="http://localhost:5000/" method="post">'+
                                                '<p>Select the analysis type:</p>' +
                                                '<div> <input type="radio" id="destination" name="analysis_type" value="destination" checked> <label for="destination"> Where trips travel from (Destination) </label> </div>' +
                                                '<div> <input type="radio" id="origin" name="analysis_type" value="origin"> <label for="origin"> Where trips travel to (Origin) </label> </div>' +
                                                '<form name="hexid" action="http://localhost:5000/" method="post">'+
                                                'ID: <input type="text" name="gridid">'+
                                                '<input type="submit" name="action" value="Submit">'+
                                                '<input type="submit" name="action" value="Vizualize">'
                            return this._div;
                }
                myControl.addTo(map);
                

                var myStyle = {
                    "color": "#ff7800",
                    "weight": 5,
                    "opacity": 0.65
                };

                function onEachFeature(feature, layer) {
                    if (feature.properties && feature.properties.h3_id) {
                        layer.bindPopup(feature.properties.h3_id);
                    }
                }

                
                // https://gis.stackexchange.com/questions/330443/loading-geojson-file-into-map-in-leaflet
                fetch("https://raw.githubusercontent.com/abdallahshabarek/JavaScript/main/Testing_file/sample2.geojson")
                // fetch("http://localhost:8000/sample.geojson")
                    .then(response => response.json())
                    .then(json => {
                        kaoDist = L.geoJSON(json,{onEachFeature: onEachFeature}).addTo(map);
                        // kaoDist.bindPopup('<h1>'+feature.properties.h3_id);
                        
                        map.fitBounds(kaoDist.getBounds());
                    });


                    // "https://stackoverflow.com/questions/17665565/is-there-a-way-to-run-r-code-from-javascript"
                    // ""
                    app.get('/sfunction', function (req, res) {
                        exec('Rscript r/Script.r', function(error, stdout, stderr) {
                            if (error) {
                                console.log(error);
                                res.send(error);
                            }
                            else if (stderr) {
                                console.log(stderr);
                                res.send(stderr);
                            }
                            else if (stdout) {
                                console.log("RAN SUCCESSFULLY");
                                res.sendfile("savedoutput/test.json");
                            }
                        });
                    });
                
                //Add base layer
                // 127.0.0.1/
                const options = {
                    method: 'GET',
                    headers: {
                    'Accept': 'application/json',
                    'Content-Type': 'application/json'
                    },
                    mode: 'no-cors'
                };
                // fetch("https://raw.githubusercontent.com/abdallahshabarek/JavaScript/main/Testing_file/sample.geojson",options)
                // .then(function (response){
                    
                //     if (!response.ok) {
                //         console.log('ERROR')
                //         console.log(response.json())
                //     }else{
                //         console.log(response)
                //         return response.json;

                //     }
                // })
                // .then(function (data){
                //     console.log(data)
                //     L.geoJSON(data).addTo(map);
                // })

                // function sleep(delay) {
                //     var start = new Date().getTime();
                //     while (new Date().getTime() < start + delay);
                // }
                // async function addGeoJson() {
                //     const response = await fetch("https://raw.githubusercontent.com/abdallahshabarek/JavaScript/main/Testing_file/sample.geojson",options);
                //     console.log(response)
                //     const data = await response.json();
                    
                //     L.geoJson(data).addTo(map);
                // }

                // addGeoJson();

                // $.ajax({
                //     // url: "http://127.0.0.1:8000/data.json",
                //     url: "https://raw.githubusercontent.com/abdallahshabarek/JavaScript/main/Testing_file/sample.geojson",
                //     crossDomain: true,
                //     headers: {'Access-Control-Allow-Origin':'*'}, 
                //     dataType: "json",
                //     type: 'GET',
                //     success: function(response) {
                //         console.log(informationArray)
                //         $.each(response.Users, function(item) {
                //         informationArray.push(item);
                //         });
                //         informationArray.push("success");
                //         console.log(informationArray)
                //     },
                //     error: function (xhr, ajaxOptions, thrownError) {
                //         alert(xhr.status);
                //         alert(thrownError);
                //     }
                //     });


            </script>
        </body>
        </html>
    '''
    return html_code