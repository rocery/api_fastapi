import { NavLink } from "react-router-dom";
import { cn } from "@/lib/utils";

const links = [
  { to: "/devices", label: "Devices" },
  { to: "/devices/speedtest", label: "ISP Speedtest" },
  { to: "/atk", label: "ATK" },
];

export function Sidebar() {
  return (
    <aside className="hidden w-56 shrink-0 border-r bg-muted/20 p-4 md:block">
      <nav className="flex flex-col gap-1">
        {links.map((l) => (
          <NavLink
            key={l.to}
            to={l.to}
            className={({ isActive }) =>
              cn("rounded-md px-3 py-2 text-sm hover:bg-accent hover:text-accent-foreground", isActive && "bg-accent text-accent-foreground font-medium")
            }
          >
            {l.label}
          </NavLink>
        ))}
      </nav>
    </aside>
  );
}
