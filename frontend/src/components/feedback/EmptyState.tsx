export function EmptyState({ message = "No data found." }: { message?: string }) {
  return <div className="py-12 text-center text-sm text-muted-foreground">{message}</div>;
}
