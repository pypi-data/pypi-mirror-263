/*

Copyright 2024 Marianna Iorio, Sonia Maffioli, Massimo Santini, Matteo Simone

This file is part of "jp²rt".

This is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This material is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this file.  If not, see <https://www.gnu.org/licenses/>.

*/

package it.unimi.di.jp2rt;

import java.util.Arrays;
import java.util.List;
import java.util.Objects;
import java.util.stream.Collectors;
import java.util.stream.DoubleStream;

public class TSVLine {
  private final String[] extra;
  private final String smiles;
  private DoubleStream descriptors = null;

  public TSVLine(final String line) {
    final String[] fields =
        Objects.requireNonNull(line, "The line parameter must not be null").split("\t");
    extra = Arrays.copyOfRange(fields, 0, fields.length - 1);
    smiles = fields[fields.length - 1];
    if (smiles.isBlank())
      throw new IllegalArgumentException(
          "The SMILES string (last field on the line) must not be blank");
  }

  public List<String> extra() {
    return Arrays.asList(extra);
  }

  public String smiles() {
    return smiles;
  }

  public double[] descriptors() {
    return descriptors.toArray();
  }

  public TSVLine descriptors(DoubleStream values) {
    this.descriptors = Objects.requireNonNull(values, "The values parameter must not be null");
    return this;
  }

  @Override
  public String toString() {
    return (extra.length > 0 ? String.join("\t", extra) + "\t" : "")
        + smiles
        + (descriptors != null
            ? "\t" + descriptors.mapToObj(Double::toString).collect(Collectors.joining("\t"))
            : "");
  }
}
