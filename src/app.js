import express from "express";
import cors from "cors";
import { connectDB } from "./db.js";
import ingredientsRoutes from "./routes/ingrediente.route.js";
import path from "path";
import { fileURLToPath } from "url";
const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const app = express();
app.use(cors());
app.use(express.json());

// Conectar a MongoDB
connectDB();

// Aquí irán tus rutas
//const ingredienteRoutes = require("./routes/ingredienteRoutes");
//app.use("/api/ingredientes", ingredienteRoutes);
app.use("/api/ingredientes", ingredientsRoutes);

const PORT = process.env.PORT || 3000;
app.use("/uploads", express.static(path.join(__dirname, "../uploads")));
app.listen(PORT, () => {
  console.log(`🚀 Servidor corriendo en puerto ${PORT}`);
});
