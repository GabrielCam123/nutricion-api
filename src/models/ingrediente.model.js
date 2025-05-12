import mongoose from "mongoose";

const ingredienteSchema = new mongoose.Schema(
  {
    nombre: { type: String, required: true, unique: true },
    tipo: { type: String, required: true },
    caloriasPor100g: { type: Number, required: true },
    proteinas: { type: Number },
    grasas: { type: Number },
    carbohidratos: { type: Number },
    fibra: { type: Number },
    sodio: { type: Number },
    agua: { type: Number },
    carbohidratosDisponibles: { type: Number },
    cenizas: { type: Number },
    potasio: { type: Number },
    calcio: { type: Number },
    fosforo: { type: Number },
    hierro: { type: Number },
    zinc: { type: Number },
    tiamina: { type: Number },
    rivoflavina: { type: Number },
    niacina: { type: Number },
    vitaminaC: { type: Number },
    acidosGrasosSaturados: { type: Number },
    acidosGrasosMonoinsaturados: { type: Number },
    acidosGrasosPoliinsaturados: { type: Number },
    colesterol: { type: Number },
    imagen: {
      type: String, // guarda el nombre o ruta del archivo
      default: null,
    }    
  },
  {
    timestamps: true,
  }
);

const Ingrediente = mongoose.model("Ingrediente", ingredienteSchema);

export default Ingrediente;
