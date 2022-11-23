import express from "express";
import indexRoutes from "./routes/index.routes";
import exphbs from "express-handlebars";
import path from "path";
import { create } from "express-handlebars";

const app = express();

app.set("views", path.join(__dirname, "views"));

var hbs = create({
  layoutsDir: path.join(app.get("views"), "layouts"),
  defaultLayout: "main",
  extname: ".hbs",
});
app.engine(".hbs", hbs.engine);

app.set("view engine", ".hbs");

app.use(indexRoutes);

export default app;
