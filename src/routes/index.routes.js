import { Router } from "express";
import users from '../models/users';

const router = Router();

router.get("/", (req, res) => {
  res.render("index");
});

router.post("/users/add", async (req, res) => {
  const users = users(req.body);

  const userSaved = await users.save()

  res.send("login user");
});

export default router;
