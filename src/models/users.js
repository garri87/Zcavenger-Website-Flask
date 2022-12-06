import { Schema, model } from "mongoose";

const userSchema = new Schema(
  {
    userID: { 
      type: Integer,
      required: true,
      autoIndex: true,
    }, 

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
       // required: true,
    },
  },
  {
    timestamps: true,
  }
);

export default model("User", userSchema);
