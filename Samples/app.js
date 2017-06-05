var express = require("express");
var path = require("path");
var fs = require("fs");
var app = express();
app.use(function(req,res,next){
  console.log("IP:", req.url);
  console.log("Request date:"+ new Date());
  next();
});

app.use(function(req,res,next){
  var filePath = path.join(__dirname__,"static",req.url);
  fs.stat(filePath,function(err,fileInfo){
    if (err){
      next();
      return
    }
    if(fileInfo.isFile()){
      res.sendFile(filePath);
    }else{
      next();
    }
  });
});

app.use(function(req,res){
  res.status(404);
  res.send("File Not Found");

});

app.listen(3000,function(){
  console.log("Aplicacion iniciada en el puerto 3000");
});
