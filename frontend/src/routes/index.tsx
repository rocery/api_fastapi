import { createBrowserRouter, Navigate } from "react-router-dom";
import { AppLayout } from "@/components/layout/AppLayout";
import { ProtectedRoute } from "./ProtectedRoute";
import { LoginPage } from "@/modules/auth/pages/LoginPage";
import { DeviceListPage } from "@/modules/device/pages/DeviceListPage";
import { IspSpeedtestPage } from "@/modules/device/pages/IspSpeedtestPage";
import { AtkListPage } from "@/modules/atk/pages/AtkListPage";

export const router = createBrowserRouter([
  { path: "/login", element: <LoginPage /> },
  {
    path: "/",
    element: (
      <ProtectedRoute>
        <AppLayout />
      </ProtectedRoute>
    ),
    children: [
      { index: true, element: <Navigate to="/devices" replace /> },
      { path: "devices", element: <DeviceListPage /> },
      { path: "devices/speedtest", element: <IspSpeedtestPage /> },
      { path: "atk", element: <AtkListPage /> },
    ],
  },
  { path: "*", element: <Navigate to="/" replace /> },
]);
