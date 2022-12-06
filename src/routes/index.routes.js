import { Router } from "express";
import Users from '../models/users';

const router = Router();

router.get("/", (req, res) => {
  res.render("index");
});

router.post("/users/add", async (req, res) => {
  const users = Users(req.body);

  const userSaved = await users.save()

  res.send("login user");

  console.log(users);
});

export default router;
