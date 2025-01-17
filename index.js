// const express = require('express');
// const multer = require('multer');
// const cors = require('cors');
// const path = require('path');
// const req = require('express/lib/request');
// const res = require('express/lib/response');

// const port = 4000;

// const app = express();

// app.use(cors());

// const uploads = multer({
//     dest: __dirname + "/uploads",
// });

// app.post("/uploads", uploads.single("image"), (req, res) => {
//     // console.log("====================")
//     const spawn = require('child_process').spawn;
//     var process = spawn('python3', ['./preprocessing/predict.py', req.file.path]);
//     var scriptData = "";
//     var errorData = "";

//     // console.log("==================== 1 ===================");
//     process.stdout.on('data', function(data){
//       //  console.log("==================== 1.1 ===================");
//         scriptData = data.toString().replace(/(\r\n|\n|\r)/gm,""); ;
//         console.log("letters", scriptData);
//     });

//     // console.log("==================== 2 ===================");

//     process.stderr.on('data', (data) => {
//         errorData = data.toString().replace(/(\r\n|\n|\r)/gm, '');
//         // console.log("==================== 2.1 ===================");
//         // console.log("Error: ++++++++++" + errorData);
//        console.error(errorData);
//     });

//     // console.log("==================== 3 ===================");
//     process.on('close', (code) => {
//         // console.log("==================== 3.1 ===================");
//         console.log(`Python script exited with code ${code}`);
//         const resp = {
//             status: "file received and processed",
//             class: scriptData,
//         };
//         res.json(resp);
//     })
// });

// app.listen(port, function(){
//     console.log("Server running on port 4000");
// })

const express = require("express");
const multer = require("multer");
const cors = require("cors");
const mongoose = require("mongoose");
const config = require("./config/database");
const letterRoutes = require("./routes/letterRoutes");
const userActivityRoutes = require("./routes/userActivityRoutes");

const app = express();

// Middleware
app.use(cors());
app.use(express.json());

const uploads = multer({
  dest: __dirname + "/uploads",
});

app.post("/uploads", uploads.single("image"), (req, res) => {
  const spawn = require("child_process").spawn;
  var process = spawn("python3", ["./preprocessing/predict.py", req.file.path]);
  var scriptData = "";
  var errorData = "";

  process.stdout.on("data", function (data) {
    scriptData = data.toString().replace(/(\r\n|\n|\r)/gm, "");
    console.log("letters", scriptData);
  });

  process.stderr.on("data", (data) => {
    errorData = data.toString().replace(/(\r\n|\n|\r)/gm, "");
    console.error(errorData);
  });

  process.on("close", (code) => {
    console.log(`Python script exited with code ${code}`);
    const resp = {
      status: "file received and processed",
      class: scriptData,
    };
    res.json(resp);
  });
});

// MongoDB Connection
mongoose
  .connect(config.db.uri)
  .then(() => console.log("Connected to MongoDB"))
  .catch((err) => console.error("Error connecting to MongoDB", err));

// Routes
app.use("/api/letters", letterRoutes);
app.use("/api/user-activities", userActivityRoutes);

// Start Server
app.listen(config.app.port, "0.0.0.0", () => {
  console.log(`Server running on port ${config.app.port}`);
});
