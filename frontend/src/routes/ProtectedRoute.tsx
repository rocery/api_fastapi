import { Navigate } from "react-router-dom";
import { useAuth } from "@/hooks/useAuth";
import { Loading } from "@/components/feedback/Loading";

export function ProtectedRoute({ children }: { children: React.ReactNode }) {
  const { isAuthenticated, isLoading, token } = useAuth();

  if (isLoading) return <Loading />;

  if (!token) return <Navigate to="/login" replace />;

  // allow rendering while user is being fetched — isAuthenticated may be false briefly
  // if token exists but user fetch failed, api interceptor already cleared auth
  if (!isAuthenticated && !isLoading) {
    // if still loading user, show loading; else redirect
    return <Navigate to="/login" replace />;
  }

  return <>{children}</>;
}
