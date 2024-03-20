// Copyright (c) Paddy Mullen
// Distributed under the terms of the Modified BSD License.
import _ from 'lodash';
import {
  DOMWidgetModel,
  DOMWidgetView,
  ISerializers,
} from '@jupyter-widgets/base';

import {
  Base64Benchmark,
  Base64SimpleDFWidget,
  BytesBenchmark,
  BytesSimpleDFWidget,
  DFDataBenchmark,
  SimpleDFWidget,
} from './SimpleDFWidget';

import * as Backbone from 'backbone';

import React, { useEffect, useState } from 'react';
import * as ReactDOMClient from 'react-dom/client';
import { MODULE_NAME, MODULE_VERSION } from './version';
// Import the CSS

export class ReactWidgetModel extends DOMWidgetModel {
  defaults(): Backbone.ObjectHash {
    return {
      ...super.defaults(),

      _model_name: ReactWidgetModel.model_name,
      _model_module: ReactWidgetModel.model_module,
      _model_module_version: ReactWidgetModel.model_module_version,
      _view_name: ReactWidgetModel.view_name,
      _view_module: ReactWidgetModel.view_module,
      _view_module_version: ReactWidgetModel.view_module_version,
    };
  }

  static serializers: ISerializers = {
    ...DOMWidgetModel.serializers,
  };

  static model_name = 'DCEFWidgetModel';
  static view_name = 'ExampleView'; // Set to null if no view
  static model_module = MODULE_NAME;
  static view_module = MODULE_NAME; // Set to null if no view
  static model_module_version = MODULE_VERSION;
  static view_module_version = MODULE_VERSION;
}

export class ReactWidgetView extends DOMWidgetView {
  rComponent: any = null;
  render(): void {
    this.el.classList.add('custom-widget');

    const Component = () => {
      const [_, setCounter] = useState(0);
      const forceRerender = () => {
        setCounter((x: number) => x + 1);
      };
      useEffect(() => {
        this.listenTo(this.model, 'change', forceRerender);
      }, []);

      const props: any = {};
      for (const key of Object.keys(this.model.attributes)) {
        props[key] = this.model.get(key);
        props['on_' + key] = (value: any) => {
          this.model.set(key, value);
          this.touch();
        };
      }
      return React.createElement(this.rComponent, props);
    };

    const root = ReactDOMClient.createRoot(this.el);
    const componentEl = React.createElement(Component, {});
    root.render(componentEl);
  }
}

export class SimpleDFWidgetView extends ReactWidgetView {
  rComponent: any = SimpleDFWidget;
}

export class BytesWidgetView extends ReactWidgetView {
  rComponent = BytesSimpleDFWidget;
}

export class Base64WidgetView extends ReactWidgetView {
  rComponent = Base64SimpleDFWidget;
}

export class BytesBenchmarkWidgetView extends ReactWidgetView {
  rComponent = BytesBenchmark;
}

export class Base64BenchmarkWidgetView extends ReactWidgetView {
  rComponent = Base64Benchmark;
}

export class DFDataBenchmarkWidgetView extends ReactWidgetView {
  rComponent = DFDataBenchmark;
}
