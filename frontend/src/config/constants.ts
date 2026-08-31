export const TOKEN_KEY = "access_token";
export const USER_KEY = "auth_user";

export const PAGINATION_DEFAULTS = {
  page: 1,
  perPage: 20,
} as const;

export const PERIOD_REGEX = /^\d{4}-(0[1-9]|1[0-2])$/;
