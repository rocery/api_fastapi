import { useState, useMemo } from "react";

export function usePagination(totalItems: number, perPage = 20) {
  const [page, setPage] = useState(1);
  const totalPages = Math.ceil(totalItems / perPage);
  const paginated = useMemo(() => ({ page, perPage, totalPages }), [page, perPage, totalPages]);
  return { ...paginated, setPage };
}
