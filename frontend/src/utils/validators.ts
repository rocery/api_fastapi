import { z } from "zod";

export const loginSchema = z.object({
  username: z.string().min(1, "Username required"),
  password: z.string().min(1, "Password required"),
});

export type LoginFormValues = z.infer<typeof loginSchema>;

export const periodSchema = z
  .string()
  .regex(/^\d{4}-(0[1-9]|1[0-2])$/, "Format must be YYYY-MM")
  .optional()
  .or(z.literal(""));
