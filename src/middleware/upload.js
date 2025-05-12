// utils/upload.js
import multer from "multer";
import path from "path";
import fs from "fs";

// Crear la carpeta si no existe
const carpetaUploads = "./uploads";
if (!fs.existsSync(carpetaUploads)) {
  fs.mkdirSync(carpetaUploads);
}

// if (!fs.existsSync(carpetaUploads)) {
//   fs.mkdirSync(carpetaUploads);
// }

const storage = multer.diskStorage({
  destination: (req, file, cb) => {
    cb(null, carpetaUploads);
  },
  filename: (req, file, cb) => {
    const nombreUnico = Date.now() + path.extname(file.originalname);
    cb(null, nombreUnico);
  },
});

export const upload = multer({ storage });
