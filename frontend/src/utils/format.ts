export function formatCurrency(value: number | null | undefined, currency = "IDR") {
  if (value == null) return "-";
  return new Intl.NumberFormat("id-ID", { style: "currency", currency }).format(value);
}

export function formatDate(value: string | Date | null | undefined) {
  if (!value) return "-";
  const d = new Date(value);
  if (isNaN(d.getTime())) return String(value);
  return new Intl.DateTimeFormat("id-ID", { dateStyle: "medium", timeStyle: "short" }).format(d);
}

export function formatNumber(value: number | null | undefined, digits = 2) {
  if (value == null) return "-";
  return Number(value).toFixed(digits);
}
