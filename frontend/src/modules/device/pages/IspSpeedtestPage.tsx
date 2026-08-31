import { useState } from "react";
import { useIspSpeedtests } from "../hooks/useIspSpeedtests";
import { IspSpeedtestTable } from "../components/IspSpeedtestTable";
import { IspSpeedtestFilter } from "../components/IspSpeedtestFilter";
import { Loading } from "@/components/feedback/Loading";
import { ErrorAlert } from "@/components/feedback/ErrorAlert";
import { EmptyState } from "@/components/feedback/EmptyState";
import { Card, CardHeader, CardTitle, CardDescription, CardContent } from "@/components/ui/card";

export function IspSpeedtestPage() {
  const [server, setServer] = useState("");
  const [period, setPeriod] = useState("");

  const { data, isLoading, error } = useIspSpeedtests({
    server: server || undefined,
    period: period || undefined,
  });

  return (
    <div className="space-y-4">
      <h1 className="text-2xl font-bold">ISP Speedtest</h1>
      <Card>
        <CardHeader>
          <CardTitle>Speedtest History</CardTitle>
          <CardDescription>Filter by server and period (YYYY-MM)</CardDescription>
          <IspSpeedtestFilter server={server} period={period} onServerChange={setServer} onPeriodChange={setPeriod} onReset={() => { setServer(""); setPeriod(""); }} />
        </CardHeader>
        <CardContent>
          {isLoading && <Loading />}
          {error && <ErrorAlert message={(error as Error).message} />}
          {!isLoading && !error && (!data || data.length === 0) && <EmptyState message="No speedtest records." />}
          {!isLoading && !error && data && data.length > 0 && <IspSpeedtestTable data={data} />}
        </CardContent>
      </Card>
    </div>
  );
}
