import { Schema, model } from "mongoose";

const userSchema = new Schema(
  {
    userName: {
        type: String,
        required: true,
        unique: true,
        trim: true,
    },
    pass: {
        type: String,
        required: true,
    },
    mail: {
        type: String,
        required: true,
    },
  },
  {
    timestamps: true,
  }
);

export default model("User", userSchema);
