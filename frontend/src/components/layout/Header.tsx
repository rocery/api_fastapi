import { useAuth } from "@/hooks/useAuth";
import { Button } from "@/components/ui/button";

export function Header() {
  const { user, logout } = useAuth();

  return (
    <header className="sticky top-0 z-10 flex h-14 items-center justify-between border-b bg-background px-4">
      <span className="font-semibold">IoT API</span>
      <div className="flex items-center gap-3">
        {user && <span className="text-sm text-muted-foreground">{user.username} ({user.level})</span>}
        {user && (
          <Button variant="outline" size="sm" onClick={logout}>
            Logout
          </Button>
        )}
      </div>
    </header>
  );
}
