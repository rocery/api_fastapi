export interface LoginRequest {
  username: string;
  password: string;
}

export interface LoginResponse {
  access_token: string;
  token_type: string;
  user: User;
}

export interface User {
  user_id: number;
  username: string;
  name: string | null;
  email: string | null;
  level: string;
  created_date?: string | null;
}
