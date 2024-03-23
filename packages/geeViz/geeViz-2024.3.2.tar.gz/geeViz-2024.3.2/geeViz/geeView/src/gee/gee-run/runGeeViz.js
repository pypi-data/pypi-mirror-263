var layerLoadErrorMessages=[];showMessage('Loading',staticTemplates.loadingModal[mode]);
function runGeeViz(){
Map.addSerializedLayer({"result": "0", "values": {"0": {"functionInvocationValue": {"functionName": "ImageCollection.load", "arguments": {"id": {"constantValue": "projects/lcms-292214/assets/Paper/Rasters_v2022-8/StandReplacing"}}}}}},{"reducer": "{\"result\": \"0\", \"values\": {\"0\": {\"functionInvocationValue\": {\"functionName\": \"Reducer.stdDev\", \"arguments\": {}}}}}", "min": 0, "max": 0.2, "canAreaChart": true, "areaChartParams": {"reducer": "{\"result\": \"0\", \"values\": {\"0\": {\"functionInvocationValue\": {\"functionName\": \"Reducer.frequencyHistogram\", \"arguments\": {}}}}}"}},'LCMS Paper Stand Replacing Transitions',true);if(layerLoadErrorMessages.length>0){showMessage("Map.addLayer Error List",layerLoadErrorMessages.join("<br>"));}
setTimeout(function(){if(layerLoadErrorMessages.length===0){$('#close-modal-button').click();}}, 2500);
Map.turnOnAutoAreaCharting();
queryWindowMode = "sidePane"
}