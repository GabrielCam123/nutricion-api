import Ingrediente from "../models/ingrediente.model.js";

// Crear nuevo ingrediente
export const crearIngrediente = async (req, res) => {
  try {
    const datos = req.body;

    if (req.file) {
      datos.imagen = req.file.filename;
    }

    const nuevoIngrediente = new Ingrediente(datos);
    const ingredienteGuardado = await nuevoIngrediente.save();
    res.status(201).json(ingredienteGuardado);
  } catch (error) {
    res.status(500).json({ mensaje: "Error al crear el ingrediente", error });
  }
  //   try {
  //   const ingredientes = req.body;

  //   if (!Array.isArray(ingredientes)) {
  //     return res.status(400).json({ mensaje: "Se esperaba un arreglo de ingredientes." });
  //   }

  //   const ingredientesGuardados = await Ingrediente.insertMany(ingredientes);
  //   res.status(201).json(ingredientesGuardados);
  // } catch (error) {
  //   console.error(error);
  //   res.status(500).json({ mensaje: "Error al crear los ingredientes", error });
  // }
};

// Obtener todos los ingredientes
export const obtenerIngredientes = async (req, res) => {
  try {
    const ingredientes = await Ingrediente.find();
    res.json(ingredientes);
  } catch (error) {
    res.status(500).json({ mensaje: "Error al obtener ingredientes", error });
  }
};

// Obtener un ingrediente por ID
export const obtenerIngredientePorId = async (req, res) => {
  try {
    const ingrediente = await Ingrediente.findById(req.params.id);
    if (!ingrediente) {
      return res.status(404).json({ mensaje: "Ingrediente no encontrado" });
    }
    res.json(ingrediente);
  } catch (error) {
    res.status(500).json({ mensaje: "Error al obtener el ingrediente", error });
  }
};

// Actualizar un ingrediente
import fs from "fs";
import path from "path";

export const actualizarIngrediente = async (req, res) => {
  try {
    const { id } = req.params;

    const ingrediente = await Ingrediente.findById(id);
    if (!ingrediente)
      return res.status(404).json({ mensaje: "Ingrediente no encontrado" });

    // Si se sube una nueva imagen, eliminamos la anterior
    if (req.file) {
      if (ingrediente.imagen) {
        const rutaImagenVieja = path.join("uploads", ingrediente.imagen);
        if (fs.existsSync(rutaImagenVieja)) {
          fs.unlinkSync(rutaImagenVieja); // elimina archivo
        }
      }
      ingrediente.imagen = req.file.filename;
    }

    // Actualizamos otros campos
    ingrediente.nombre = req.body.nombre || ingrediente.nombre;
    ingrediente.tipo = req.body.tipo || ingrediente.tipo;
    ingrediente.caloriasPor100g =
      req.body.caloriasPor100g || ingrediente.caloriasPor100g;

    await ingrediente.save();
    res.json(ingrediente);
  } catch (error) {
    console.error("Error actualizando ingrediente:", error);
    res.status(500).json({ mensaje: "Error del servidor" });
  }
};

// Eliminar un ingrediente
export const eliminarIngrediente = async (req, res) => {
  try {
    const eliminado = await Ingrediente.findByIdAndDelete(req.params.id);
    if (!eliminado) {
      return res.status(404).json({ mensaje: "Ingrediente no encontrado" });
    }
    res.json({ mensaje: "Ingrediente eliminado" });
  } catch (error) {
    res
      .status(500)
      .json({ mensaje: "Error al eliminar el ingrediente", error });
  }
};
