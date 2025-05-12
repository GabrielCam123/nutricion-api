import mongoose from "mongoose";

export const connectDB = async () => {
  try {
    await mongoose.connect(
      "mongodb://admin:Password1@127.0.0.1:27017/tudespensa",
      {
        authSource: "admin", // importante: de dónde viene el usuario
      }
    );
    console.log("✅ Conectado a MongoDB");
  } catch (error) {
    console.error("❌ Error al conectar a MongoDB:", error);
    process.exit(1);
  }
};
