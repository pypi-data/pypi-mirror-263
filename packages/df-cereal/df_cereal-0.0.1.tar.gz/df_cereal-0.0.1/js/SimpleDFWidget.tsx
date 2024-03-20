import React from 'react';
//import React, { useState, useRef } from 'react';
import _ from 'lodash';

import { tableFromIPC } from 'apache-arrow';
import { arrowFromBase64, arrowToDFDataProxy } from './arrowUtils';

export type DFDataRow = Record<
  string,
  string | number | boolean | any | null
  // | any[] | Record<string, any>
>;

export type DFData = DFDataRow[];

function tableRow(r: DFDataRow) {
  return Object.keys(r).map((key: string) => {
    const val = r[key];
    return <td key={key}> {val ? val.toString() : 'None'} </td>;
  });
}

function headerRow(r: DFDataRow) {
  return Object.keys(r).map((key: string) => {
    return <th key={key}> {key} </th>;
  });
}

export function SimpleDFWidget({ df_data }: { df_data: DFData }) {
  console.log('SimpleDFWidget');
  if (df_data.length === 0) {
    return <h3> empty df_data</h3>;
  }

  return (
    <div>
      <table>
        <thead>
          <tr>{headerRow(df_data[0])}</tr>
        </thead>
        <tbody>
          {df_data.map((valDict, index) => {
            return <tr key={index}>{tableRow(valDict)}</tr>;
          })}
        </tbody>
      </table>
    </div>
  );
}

export function BytesSimpleDFWidgetOrig({
  df_arrow_bytes,
}: {
  df_arrow_bytes: any;
}) {
  console.log('df_arrow_bytes', df_arrow_bytes);
  const table = tableFromIPC(df_arrow_bytes);
  console.log('table', table);
  const dfd: DFData = arrowToDFDataProxy(table);
  return SimpleDFWidget({ df_data: dfd });
}

export function BytesSimpleDFWidget({
  df_arrow_bytes,
}: {
  df_arrow_bytes: DataView;
}) {
  console.log('df_arrow_bytes', df_arrow_bytes);
  //const uintBytes = new Uint8Array(df_arrow_bytes.buffer);
  // bigInts don't print normally, have to call .toString() on them

  const table = tableFromIPC(df_arrow_bytes.buffer); //uintBytes);
  console.log('table', table);
  const dfd: DFData = arrowToDFDataProxy(table);
  return SimpleDFWidget({ df_data: dfd });
}

export function Base64SimpleDFWidget({ df_base64 }: { df_base64: string }) {
  const table = arrowFromBase64(df_base64);
  //  const table = tableFromIPC(df_arrow_bytes);

  const dfd: DFData = arrowToDFDataProxy(table);
  return SimpleDFWidget({ df_data: dfd });
}

export const proxyIterate = (df_data: DFData) => {
  //fast function that requires accessing each element of df_data
  let accum = 0;
  for (let i = 0; i < df_data.length; i++) {
    const row = df_data[i];

    _.forEach(row, (val) => {
      if (val === null) {
        return;
      }
      if (typeof val === 'string') {
        accum += val.length;
      } else if (typeof val === 'number') {
        accum += val;
      }
    });

    //console.log("row", row)
  }
  return accum;
};

export const BytesBenchmark = ({
  df_arrow_bytes,
  timing_info,
  on_timing_info,
  do_calc,
  message,
}: {
  df_arrow_bytes: DataView;
  timing_info: any;
  on_timing_info: any;
  do_calc: boolean;
  message: string;
}) => {
  console.log('Bytes Benchmark', _.keys(timing_info).length, do_calc);
  if (_.keys(timing_info).length === 0 && do_calc) {
    const t1 = new Date();
    const table = tableFromIPC(df_arrow_bytes.buffer); //uintBytes);
    const dfd: DFData = arrowToDFDataProxy(table);
    const t2 = new Date();
    console.log('proxyIterate', proxyIterate(dfd));
    const t3 = new Date();
    //@ts-ignore
    const d1 = t2 - t1;
    //@ts-ignore
    const d2 = t3 - t2;
    console.log('d1', d1, 'd2', d2);
    on_timing_info({ t1, t2, t3 });
    console.log('bytesBenchmark finished');
  }
  return <h1> Bytes Benchmark: {message}</h1>;
};

export const Base64Benchmark = ({
  df_base64,
  timing_info,
  on_timing_info,
  do_calc,
  message,
}: {
  df_base64: string;
  timing_info: any;
  on_timing_info: any;
  do_calc: boolean;
  message: string;
}) => {
  console.log('Base64 benchmark', _.keys(timing_info).length, do_calc);
  if (_.keys(timing_info).length === 0 && do_calc) {
    const t1 = new Date();
    const table = arrowFromBase64(df_base64);
    const dfd: DFData = arrowToDFDataProxy(table);
    const t2 = new Date();
    console.log('proxyIterate', proxyIterate(dfd));
    const t3 = new Date();
    //@ts-ignore
    const d1 = t2 - t1;
    //@ts-ignore
    const d2 = t3 - t2;
    console.log('d1', d1, 'd2', d2);
    on_timing_info({ t1, t2, t3 });
    console.log('Base64 Benchmark finished');
  }
  return <h1> Base64 Benchmark: {message}</h1>;
};

export const DFDataBenchmark = ({
  df_data,
  timing_info,
  on_timing_info,
  do_calc,
  message,
}: {
  df_data: DFData;
  timing_info: any;
  on_timing_info: any;
  do_calc: boolean;
  message: string;
}) => {
  console.log('Base64 benchmark', _.keys(timing_info).length, do_calc);
  if (_.keys(timing_info).length === 0 && do_calc) {
    const t1 = new Date();
    const t2 = new Date();
    console.log('proxyIterate', proxyIterate(df_data));
    const t3 = new Date();
    //@ts-ignore
    const d1 = t2 - t1;
    //@ts-ignore
    const d2 = t3 - t2;
    console.log('d1', d1, 'd2', d2);
    on_timing_info({ t1, t2, t3 });
    console.log('DFDataBenchmark finished');
  }
  return <h1> DFData Benchmark: {message}</h1>;
};
