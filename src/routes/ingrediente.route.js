import { Router } from "express";
import {
  crearIngrediente,
  obtenerIngredientes,
  obtenerIngredientePorId,
  actualizarIngrediente,
  eliminarIngrediente,
} from "../controllers/ingrediente.controller.js";
import { upload } from "../middleware/upload.js";

const router = Router();

router.post("/", upload.single("imagen"), crearIngrediente);
router.get("/", obtenerIngredientes);
router.get("/:id", obtenerIngredientePorId);
router.put("/:id", upload.single("imagen"), actualizarIngrediente);
router.delete("/:id", eliminarIngrediente);

export default router;
