from __future__ import annotations
from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional, Union
from energyml.eml.v2_3.commonv2 import (
    AbstractBooleanArray,
    AbstractFloatingPointArray,
    AbstractGraphicalInformation,
    AbstractIntegerArray,
    AbstractObject,
    AbstractValueArray,
    BooleanExternalArray,
    DataObjectReference,
    ExternalDataArray,
    FloatingPointLatticeArray,
    GeologicTime,
    IndexableElement,
    IntegerExternalArray,
    IntegerLatticeArray,
    JaggedArray,
    LegacyUnitOfMeasure,
    LengthMeasure,
    LengthMeasureExt,
    LithologyKind,
    MdInterval,
    NorthReferenceKind,
    PlaneAngleMeasure,
    PropertyKindFacet,
    StringExternalArray,
    TimeIndex,
    TimeOrIntervalSeries,
    UnitOfMeasure,
    VolumeUom,
)

__NAMESPACE__ = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class AbstractParametricLineArray:
    """Defines an array of parametric lines.

    The array size is obtained from context. In the current schema, this
    may be as simple as a 1D array (#Lines=count) or a 2D array #Lines =
    NIL x NJL for an IJK grid representation.
    """


@dataclass
class AbstractPoint3DArray:
    """The abstract class of 3D points implemented in a single fashion for the
    schema.

    Abstraction allows a variety of instantiations for efficiency or to
    implicitly provide additional geometric information about a data-
    object. For example, parametric points can be used to implicitly
    define a wellbore trajectory using an underlying parametric line, by
    the specification of the control points along the parametric line.
    The dimensionality of the array of 3D points is based on context
    within an instance.
    """

    class Meta:
        name = "AbstractPoint3dArray"


@dataclass
class AbstractSurfaceFrameworkContact:
    """
    Parent class of the sealed and non-sealed contact elements.

    :ivar index: The index of the contact. Indicates identity of the
        contact in the surface framework context. It is used for contact
        identities and to find the interpretation of this particular
        contact.
    """

    index: Optional[int] = field(
        default=None,
        metadata={
            "name": "Index",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
            "min_inclusive": 0,
        },
    )


@dataclass
class AbstractTimeInterval:
    """The abstract superclass for all RESQML time intervals.

    The super class that contains all types of intervals considered in
    geolog, including  those based on chronostratigraphy, the duration
    of geological events, and time intervals used in reservoir
    simulation (e.g., time step).
    """


class CellShape(Enum):
    """Used to indicate that all cells are of a uniform topology, i.e., have the
    same number of nodes per cell.

    This information is supplied by the RESQML writer to indicate the complexity of the grid geometry, as an aide to the RESQML reader.
    If a specific cell shape is not appropriate, then use polyhedral.
    BUSINESS RULE: Should be consistent with the actual geometry of the grid.

    :cvar TETRAHEDRAL: All grid cells are constrained to have only 4
        nodes/cell with 4 faces/cell, 3 nodes/face, 4 nodes/cell for all
        cells (degeneracy allowed).
    :cvar PYRAMIDAL: All grid cells are constrained to have only 5
        nodes/cell with 5 faces/cell, with 1 quadrilateral face and 4
        triangular faces.
    :cvar PRISM: All grid cells are constrained to have 6 nodes/cell
        with 5 faces/cell, with 3 quadrilateral faces and 2 non-adjacent
        triangular faces, as in a column layer grid with triangular
        columns.
    :cvar HEXAHEDRAL: All grid cells are constrained to have 8
        nodes/cell with 6 faces/cell, 4 nodes/face, 8 nodes/cell for all
        cells (degeneracy allowed). Equivalent to IJK grid cells.
    :cvar POLYHEDRAL: If the cell geometry is not of a more specific
        kind, use polyhedral.
    """

    TETRAHEDRAL = "tetrahedral"
    PYRAMIDAL = "pyramidal"
    PRISM = "prism"
    HEXAHEDRAL = "hexahedral"
    POLYHEDRAL = "polyhedral"


class ColumnShape(Enum):
    """Used to indicate that all columns are of a uniform topology, i.e., have the
    same number of faces per column.

    This information is supplied by the RESQML writer to indicate the complexity of the grid geometry, as an aide to the RESQML reader.
    If a specific column shape is not appropriate, then use polygonal.
    BUSINESS RULE: Should be consistent with the actual geometry of the grid.

    :cvar TRIANGULAR: All grid columns have 3 sides.
    :cvar QUADRILATERAL: All grid columns have 4 sides. Includes tartan
        and corner point grids.
    :cvar POLYGONAL: At least one grid column is a polygon, N&gt;4.
    """

    TRIANGULAR = "triangular"
    QUADRILATERAL = "quadrilateral"
    POLYGONAL = "polygonal"


class ContactMode(Enum):
    """An optional second qualifier that may be used when describing binary contact
    interpretation parts.

    (See also BinaryContactInterpretationPart and the RESQML Technical
    Usage Guide.)
    """

    CONFORMABLE = "conformable"
    EXTENDED = "extended"
    UNCONFORMABLE = "unconformable"


class ContactSide(Enum):
    """Enumeration that specifies the location of the contacts, chosen from the
    attributes listed below.

    For example, if you specify contact between a horizon and a fault, you can specify if the contact is on the foot wall side or the hanging wall side of the fault, and if the fault is splitting both sides of a horizon or the older side only.
    From Wikipedia: http://en.wikipedia.org/wiki/Foot_wall
    CC-BY-SA-3.0-MIGRATED; GFDL-WITH-DISCLAIMERS
    Released under the GNU Free Documentation License.

    :cvar FOOTWALL: The footwall side of the fault. See picture.
    :cvar HANGING_WALL:
    :cvar NORTH: For a vertical fault, specification of the north side.
    :cvar SOUTH: For a vertical fault, specification of the south side.
    :cvar EAST: For a vertical fault, specification of the east side.
    :cvar WEST: For a vertical fault, specification of the west side.
    :cvar YOUNGER: Indicates that a fault splits a genetic boundary on
        its younger side.
    :cvar OLDER: Indicates that a fault splits a genetic boundary on its
        older side.
    :cvar BOTH: Indicates that a fault splits both sides of a genetic
        feature.
    """

    FOOTWALL = "footwall"
    HANGING_WALL = "hanging wall"
    NORTH = "north"
    SOUTH = "south"
    EAST = "east"
    WEST = "west"
    YOUNGER = "younger"
    OLDER = "older"
    BOTH = "both"


class ContactVerb(Enum):
    """
    Enumerations for the verbs that can be used to define the impact on the
    construction of the model of the geological event that created the binary
    contact.

    :cvar STOPS: Specifies that an interpretation stops/interrupts
        another interpretation. Used for tectonic boundary vs tectonic
        boundary but also genetic boundary vs genetic boundary (erosion
        case), frontier vs interpretation, etc.
    :cvar SPLITS: Specifies that the fault has opened a pair of fault
        lips in a horizon or separated a geologic unit into two parts.
    :cvar CROSSES: Specifies that a tectonic boundary interpretation
        crosses another tectonic boundary interpretation.
    """

    STOPS = "stops"
    SPLITS = "splits"
    CROSSES = "crosses"


@dataclass
class CorrectionInformation:
    """
    Occurs only if a correction has been applied on the survey wellbore.

    :ivar correction_average_velocity: The UOM is composed by: UOM of
        the LocalDepth3dCrs of the associated wellbore frame trajectory
        / UOM of the associated LocalTime3dCrs. If not used, enter zero.
    :ivar correction_time_shift: The UOM is the one specified in the
        LocalTime3dCrs. If not used, enter zero.
    """

    correction_average_velocity: float = field(
        default=0.0,
        metadata={
            "name": "CorrectionAverageVelocity",
            "type": "Attribute",
        },
    )
    correction_time_shift: float = field(
        default=0.0,
        metadata={
            "name": "CorrectionTimeShift",
            "type": "Attribute",
        },
    )


class CulturalFeatureKind(Enum):
    """
    The enumeration of the possible cultural feature.
    """

    FIELDBLOCK = "fieldblock"
    LICENSES = "licenses"
    PIPELINE = "pipeline"
    PROJECT_BOUNDARIES = "project boundaries"
    MODEL_FRONTIER = "model frontier"


class DepositionMode(Enum):
    """
    Specifies the position of the stratification of a stratigraphic unit with
    respect to its top and bottom boundaries.
    """

    PROPORTIONAL_BETWEEN_TOP_AND_BOTTOM = "proportional between top and bottom"
    PARALLEL_TO_BOTTOM = "parallel to bottom"
    PARALLEL_TO_TOP = "parallel to top"
    PARALLEL_TO_ANOTHER_BOUNDARY = "parallel to another boundary"


class DepositionalEnvironmentKind(Enum):
    CONTINENTAL = "continental"
    PARALIC_SHALLOW_MARINE = "paralic shallow marine"
    DEEP_MARINE = "deep marine"
    CARBONATE_CONTINENTAL = "carbonate continental"
    CARBONATE_PARALIC_SHALLOW_MARINE = "carbonate paralic shallow marine"
    CARBONATE_DEEP_MARINE = "carbonate deep marine"


class DepositionalFaciesKind(Enum):
    CARBONATES = "carbonates"
    CARBONATES_BASINAL = "carbonates basinal"
    CARBONATES_FORESLOPE = "carbonates foreslope"
    CARBONATES_FORESLOPE_PELAGIC = "carbonates foreslope pelagic"
    CARBONATES_FORESLOPE_TURBIDITE = "carbonates foreslope turbidite"
    CARBONATES_HIGHENERGY = "carbonates highenergy"
    CARBONATES_HIGHENERGY_PLATFORM = "carbonates highenergy platform"
    CARBONATES_HIGHENERGY_PLATFORM_INTERIOR = (
        "carbonates highenergy platform interior"
    )
    CARBONATES_HIGHENERGY_PLATFORM_MARGIN = (
        "carbonates highenergy platform margin"
    )
    CARBONATES_HIGHENERGY_RAMP = "carbonates highenergy ramp"
    CARBONATES_HIGHENERGY_RAMP_INNER = "carbonates highenergy ramp inner"
    CARBONATES_HIGHENERGY_RAMP_MIDDLE = "carbonates highenergy ramp middle"
    CARBONATES_HIGHENERGY_RAMP_OUTER = "carbonates highenergy ramp outer"
    CARBONATES_HIGHENERGY_SHELF = "carbonates highenergy shelf"
    CARBONATES_HIGHENERGY_SHELF_INTERIOR = (
        "carbonates highenergy shelf interior"
    )
    CARBONATES_HIGHENERGY_SHELF_MARGIN = "carbonates highenergy shelf margin"
    CARBONATES_HIGHENERGY_SLOPE = "carbonates highenergy slope"
    CARBONATES_HIGHENERGY_SLOPE_DISTAL = "carbonates highenergy slope distal"
    CARBONATES_HIGHENERGY_SLOPE_LOWER = "carbonates highenergy slope lower"
    CARBONATES_HIGHENERGY_SLOPE_UPPER = "carbonates highenergy slope upper"
    CARBONATES_LACUSTRINE = "carbonates lacustrine"
    CARBONATES_LACUSTRINE_ABIOTIC = "carbonates lacustrine abiotic"
    CARBONATES_LACUSTRINE_BASINAL = "carbonates lacustrine basinal"
    CARBONATES_LACUSTRINE_ORGANICBUILDUP = (
        "carbonates lacustrine organicbuildup"
    )
    CARBONATES_LACUSTRINE_RAMP = "carbonates lacustrine ramp"
    CARBONATES_LACUSTRINE_RAMP_INNER = "carbonates lacustrine ramp inner"
    CARBONATES_LACUSTRINE_RAMP_MIDDLE = "carbonates lacustrine ramp middle"
    CARBONATES_LACUSTRINE_RAMP_OUTER = "carbonates lacustrine ramp outer"
    CARBONATES_LACUSTRINE_SHELF = "carbonates lacustrine shelf"
    CARBONATES_LACUSTRINE_SHELF_INTERIOR = (
        "carbonates lacustrine shelf interior"
    )
    CARBONATES_LACUSTRINE_SHELF_MARGIN = "carbonates lacustrine shelf margin"
    CARBONATES_LACUSTRINE_SHELF_SLOPE = "carbonates lacustrine shelf slope"
    CARBONATES_LACUSTRINE_SHELF_SLOPE_DISTAL = (
        "carbonates lacustrine shelf slope distal"
    )
    CARBONATES_LACUSTRINE_SHELF_SLOPE_LOWER = (
        "carbonates lacustrine shelf slope lower"
    )
    CARBONATES_LACUSTRINE_SHELF_SLOPE_UPPER = (
        "carbonates lacustrine shelf slope upper"
    )
    CARBONATES_LOWENERGY = "carbonates lowenergy"
    CARBONATES_LOWENERGY_RAMP = "carbonates lowenergy ramp"
    CARBONATES_LOWENERGY_SABKHA = "carbonates lowenergy sabkha"
    CARBONATES_LOWENERGY_SHELF = "carbonates lowenergy shelf"
    CARBONATES_LOWENERGY_TIDALFLAT = "carbonates lowenergy tidalflat"
    CARBONATES_ORGANICBUILDUP = "carbonates organicbuildup"
    CARBONATES_ORGANICBUILDUP_BANK = "carbonates organicbuildup bank"
    CARBONATES_ORGANICBUILDUP_REEF = "carbonates organicbuildup reef"
    CARBONATES_ORGANICBUILDUP_REEF_MOUND = (
        "carbonates organicbuildup reef mound"
    )
    CARBONATES_ORGANICBUILDUP_REEF_PATCH = (
        "carbonates organicbuildup reef patch"
    )
    CARBONATES_ORGANICBUILDUP_REEF_PINNACLE = (
        "carbonates organicbuildup reef pinnacle"
    )
    CARBONATES_SUBAERIAL = "carbonates subaerial"
    CONTINENTAL = "continental"
    CONTINENTAL_ALLUVIAL = "continental alluvial"
    CONTINENTAL_ALLUVIAL_DEBRISFLOW = "continental alluvial debrisflow"
    CONTINENTAL_ALLUVIAL_SHEETFLOW = "continental alluvial sheetflow"
    CONTINENTAL_EOLIAN = "continental eolian"
    CONTINENTAL_EOLIAN_ERG = "continental eolian erg"
    CONTINENTAL_EOLIAN_MIXEDEOLIANFLUVIAL = (
        "continental eolian mixedeolianfluvial"
    )
    CONTINENTAL_EOLIAN_MIXEDEOLIANSABKHA = (
        "continental eolian mixedeoliansabkha"
    )
    CONTINENTAL_FLUVIAL = "continental fluvial"
    CONTINENTAL_FLUVIAL_ALLUVIALPLAIN = "continental fluvial alluvialplain"
    CONTINENTAL_FLUVIAL_RIVER = "continental fluvial river"
    CONTINENTAL_FLUVIAL_RIVER_ANASTOMOSING = (
        "continental fluvial river anastomosing"
    )
    CONTINENTAL_FLUVIAL_RIVER_BRAIDED = "continental fluvial river braided"
    CONTINENTAL_FLUVIAL_RIVER_MEANDERING = (
        "continental fluvial river meandering"
    )
    CONTINENTAL_FLUVIAL_RIVER_STRAIGHT = "continental fluvial river straight"
    CONTINENTAL_GLACIAL = "continental glacial"
    CONTINENTAL_LACUSTRINE = "continental lacustrine"
    CONTINENTAL_LACUSTRINE_BARRIER = "continental lacustrine barrier"
    CONTINENTAL_LACUSTRINE_BEACH = "continental lacustrine beach"
    CONTINENTAL_LACUSTRINE_DELTA_BRAIDED = (
        "continental lacustrine delta braided"
    )
    CONTINENTAL_LACUSTRINE_DELTA_FAN = "continental lacustrine delta fan"
    CONTINENTAL_LACUSTRINE_SUBLACUSTRINEFAN = (
        "continental lacustrine sublacustrinefan"
    )
    DEEPMARINE = "deepmarine"
    DEEPMARINE_ABYSAL = "deepmarine abysal"
    DEEPMARINE_CHANNELCOMPLEX = "deepmarine channelcomplex"
    DEEPMARINE_CHANNELCOMPLEX_CONFINED = "deepmarine channelcomplex confined"
    DEEPMARINE_CHANNELCOMPLEX_CONFINED_CHANNELFILL = (
        "deepmarine channelcomplex confined channelfill"
    )
    DEEPMARINE_CHANNELCOMPLEX_CONFINED_LEVEE = (
        "deepmarine channelcomplex confined levee"
    )
    DEEPMARINE_CHANNELCOMPLEX_DISTRIBUTARY = (
        "deepmarine channelcomplex distributary"
    )
    DEEPMARINE_CHANNELCOMPLEX_DISTRIBUTARY_CHANNELFILL = (
        "deepmarine channelcomplex distributary channelfill"
    )
    DEEPMARINE_CHANNELCOMPLEX_DISTRIBUTARY_LEVEE = (
        "deepmarine channelcomplex distributary levee"
    )
    DEEPMARINE_CHANNELCOMPLEX_DISTRIBUTARY_LOBE = (
        "deepmarine channelcomplex distributary lobe"
    )
    DEEPMARINE_CHANNELCOMPLEX_EROSIVEAGGRADATIONAL = (
        "deepmarine channelcomplex erosiveaggradational"
    )
    DEEPMARINE_CHANNELCOMPLEX_EROSIVEAGGRADATIONAL_CHANNELFILL = (
        "deepmarine channelcomplex erosiveaggradational channelfill"
    )
    DEEPMARINE_CHANNELCOMPLEX_EROSIVEAGGRADATIONAL_DEBRITE = (
        "deepmarine channelcomplex erosiveaggradational debrite"
    )
    DEEPMARINE_CHANNELCOMPLEX_EROSIVEAGGRADATIONAL_LEVEE = (
        "deepmarine channelcomplex erosiveaggradational levee"
    )
    DEEPMARINE_CHANNELCOMPLEX_EROSIVEAGGRADATIONAL_OVERBANKDEPOSIT = (
        "deepmarine channelcomplex erosiveaggradational overbankdeposit"
    )
    DEEPMARINE_CONOURITEDRIFT = "deepmarine conouritedrift"
    DEEPMARINE_CONOURITEDRIFT_MOATMOUND = "deepmarine conouritedrift moatmound"
    DEEPMARINE_CONOURITEDRIFT_PLASTERED = "deepmarine conouritedrift plastered"
    DEEPMARINE_CONOURITEDRIFT_SHEETLIKE = "deepmarine conouritedrift sheetlike"
    DEEPMARINE_INJECTITE = "deepmarine injectite"
    DEEPMARINE_INTRASLOPEBASIN = "deepmarine intraslopebasin"
    DEEPMARINE_MASSTRANSPORTDEPOSIT = "deepmarine masstransportdeposit"
    DEEPMARINE_PELAGIC = "deepmarine pelagic"
    DEEPMARINE_SHELF = "deepmarine shelf"
    DEEPMARINE_SHELF_EDGE = "deepmarine shelf edge"
    DEEPMARINE_SLOPE = "deepmarine slope"
    DEEPMARINE_SLOPE_LOWER = "deepmarine slope lower"
    DEEPMARINE_SLOPE_UPPER = "deepmarine slope upper"
    DEEPMARINE_TURBIDITECONTOURITE = "deepmarine turbiditecontourite"
    DEEPMARINE_TURBIDITECONTOURITE_CONFINED = (
        "deepmarine turbiditecontourite confined"
    )
    DEEPMARINE_TURBIDITECONTOURITE_DISTRIBUTARY = (
        "deepmarine turbiditecontourite distributary"
    )
    MARINESHALLOW = "marineshallow"
    MARINESHALLOW_BARRIERISLAND = "marineshallow barrierisland"
    MARINESHALLOW_BARRIERISLAND_WAVEINFLUENCED = (
        "marineshallow barrierisland waveinfluenced"
    )
    MARINESHALLOW_BAY = "marineshallow bay"
    MARINESHALLOW_COAST = "marineshallow coast"
    MARINESHALLOW_COAST_TIDEDOMINATED = "marineshallow coast tidedominated"
    MARINESHALLOW_COASTALPLAIN = "marineshallow coastalplain"
    MARINESHALLOW_DELTA = "marineshallow delta"
    MARINESHALLOW_DELTA_BRAIDED = "marineshallow delta braided"
    MARINESHALLOW_DELTA_FAN = "marineshallow delta fan"
    MARINESHALLOW_DELTA_FLUVIALDOMINATED = (
        "marineshallow delta fluvialdominated"
    )
    MARINESHALLOW_DELTA_FLUVIALINFLUENCED = (
        "marineshallow delta fluvialinfluenced"
    )
    MARINESHALLOW_DELTA_TIDEDOMINATED = "marineshallow delta tidedominated"
    MARINESHALLOW_DELTA_TIDEINFLUENCED = "marineshallow delta tideinfluenced"
    MARINESHALLOW_DELTA_WAVEDOMINATED = "marineshallow delta wavedominated"
    MARINESHALLOW_DELTA_WAVEINFLUENCED = "marineshallow delta waveinfluenced"
    MARINESHALLOW_LAGON = "marineshallow lagon"
    MARINESHALLOW_LAGON_WAVEDOMINATED = "marineshallow lagon wavedominated"
    MARINESHALLOW_SHORELINE = "marineshallow shoreline"
    MARINESHALLOW_SHORELINE_ESTUARY = "marineshallow shoreline estuary"
    MARINESHALLOW_SHORELINE_ESTUARY_FLUVIALDOMINATED = (
        "marineshallow shoreline estuary fluvialdominated"
    )
    MARINESHALLOW_SHORELINE_ESTUARY_FLUVIALINFLUENCED = (
        "marineshallow shoreline estuary fluvialinfluenced"
    )
    MARINESHALLOW_SHORELINE_ESTUARY_MIXEDINFLUENCED = (
        "marineshallow shoreline estuary mixedinfluenced"
    )
    MARINESHALLOW_SHORELINE_ESTUARY_TIDEDOMINATED = (
        "marineshallow shoreline estuary tidedominated"
    )
    MARINESHALLOW_SHORELINE_ESTUARY_TIDEINFLUENCED = (
        "marineshallow shoreline estuary tideinfluenced"
    )
    MARINESHALLOW_SHORELINE_ESTUARY_WAVEDOMINATED = (
        "marineshallow shoreline estuary wavedominated"
    )
    MARINESHALLOW_SHORELINE_ESTUARY_WAVEINFLUENCED = (
        "marineshallow shoreline estuary waveinfluenced"
    )
    MARINESHALLOW_SHORELINE_SHOREFACE = "marineshallow shoreline shoreface"
    MARINESHALLOW_SHORELINE_SHOREFACE_FORESHORE = (
        "marineshallow shoreline shoreface foreshore"
    )
    MARINESHALLOW_SHORELINE_SHOREFACE_LOWER = (
        "marineshallow shoreline shoreface lower"
    )
    MARINESHALLOW_SHORELINE_SHOREFACE_MIDDLE = (
        "marineshallow shoreline shoreface middle"
    )
    MARINESHALLOW_SHORELINE_SHOREFACE_OFFSHORE = (
        "marineshallow shoreline shoreface offshore"
    )
    MARINESHALLOW_SHORELINE_SHOREFACE_UPPER = (
        "marineshallow shoreline shoreface upper"
    )
    MARINESHALLOW_SHORELINE_SHORELINE_FLUVIALDOMINATED = (
        "marineshallow shoreline shoreline fluvialdominated"
    )
    MARINESHALLOW_SHORELINE_SHORELINE_FLUVIALINFLUENCED = (
        "marineshallow shoreline shoreline fluvialinfluenced"
    )
    MARINESHALLOW_SHORELINE_SHORELINE_MIXEDINFLUENCED = (
        "marineshallow shoreline shoreline mixedinfluenced"
    )
    MARINESHALLOW_SHORELINE_SHORELINE_TIDEDOMINATED = (
        "marineshallow shoreline shoreline tidedominated"
    )
    MARINESHALLOW_SHORELINE_SHORELINE_TIDEINFLUENCED = (
        "marineshallow shoreline shoreline tideinfluenced"
    )
    MARINESHALLOW_SHORELINE_SHORELINE_WAVEDOMINATED = (
        "marineshallow shoreline shoreline wavedominated"
    )
    MARINESHALLOW_SHORELINE_SHORELINE_WAVEINFLUENCED = (
        "marineshallow shoreline shoreline waveinfluenced"
    )
    MARINESHALLOW_STRANDPLAIN = "marineshallow strandplain"
    MARINESHALLOW_TIDALFLAT = "marineshallow tidalflat"


class DisplaySpace(Enum):
    DEVICE = "device"
    MODEL = "model"


class Domain(Enum):
    """An enumeration that specifies in which domain the interpretation of an AbstractFeature has been performed: depth, time, or mixed (= depth + time).

    :cvar DEPTH: Position defined by measurements in the depth domain.
    :cvar TIME: Position based on geophysical measurements in two-way
        time (TWT).
    :cvar MIXED: depth + time
    """

    DEPTH = "depth"
    TIME = "time"
    MIXED = "mixed"


class EdgePattern(Enum):
    """
    The graphical patterns that an edge can support.

    :cvar DASHED: The edge will display as a dashed (succession of
        dashes) line.
    :cvar DOTTED: The edge will display as a dotted (succession of dots)
        line.
    :cvar SOLID: The edge will display as a single line.
    :cvar WAVY: The edge will display as a wavy line.
    """

    DASHED = "dashed"
    DOTTED = "dotted"
    SOLID = "solid"
    WAVY = "wavy"


class FluidContact(Enum):
    """
    Enumerated values used to indicate a specific type of fluid boundary
    interpretation.

    :cvar FREE_WATER_CONTACT: A surface defined by vanishing capillary
        pressure between the water and hydrocarbon phases.
    :cvar GAS_OIL_CONTACT: A surface defined by vanishing capillary
        pressure between the gas and oil hydrocarbon phases.
    :cvar GAS_WATER_CONTACT: A surface defined by vanishing capillary
        pressure between the water and gas hydrocarbon phases.
    :cvar SEAL: Identifies a break in the hydrostatic column.
    :cvar WATER_OIL_CONTACT: A surface defined by vanishing capillary
        pressure between the water and oil hydrocarbon phases.
    """

    FREE_WATER_CONTACT = "free water contact"
    GAS_OIL_CONTACT = "gas oil contact"
    GAS_WATER_CONTACT = "gas water contact"
    SEAL = "seal"
    WATER_OIL_CONTACT = "water oil contact"


class FluidMarker(Enum):
    """
    The various fluids a well marker can indicate.
    """

    GAS_DOWN_TO = "gas down to"
    GAS_UP_TO = "gas up to"
    OIL_DOWN_TO = "oil down to"
    OIL_UP_TO = "oil up to"
    WATER_DOWN_TO = "water down to"
    WATER_UP_TO = "water up to"


class GeologicBoundaryKind(Enum):
    """
    The various geologic boundaries a well marker can indicate.
    """

    FAULT = "fault"
    GEOBODY = "geobody"
    HORIZON = "horizon"


class GeologicUnitMaterialEmplacement(Enum):
    """
    The enumerated attributes of a horizon.
    """

    INTRUSIVE = "intrusive"
    NON_INTRUSIVE = "non-intrusive"


class GridGeometryAttachment(Enum):
    """
    Indexable grid elements to which point geometry may be attached to describe
    additional grid geometry.

    :cvar CELLS: Geometry may be attached to cells to distort the
        geometry of that specific cell, only (finite element grid).
    :cvar EDGES: Geometry may be attached to edges to distort the
        geometry of all cells that refer to that edge (finite element
        grid). BUSINESS RULE: The edges indexing must be known or
        defined in the grid representation if geometry is attached to
        the edges.
    :cvar FACES: Geometry may be attached to faces to distort the
        geometry of all cells that refer to that face (finite element
        grid). BUSINESS RULE: The faces indexing must be known or
        defined in the grid representation if geometry is attached to
        the faces.
    :cvar HINGE_NODE_FACES: For column layer grids, these are the K
        faces. For unstructured grids these faces are enumerated as the
        hinge node faces.
    :cvar NODES: Additional grid geometry may be attached to split or
        truncated node patches for column layer grids. All other node
        geometry attachment should be done through the Points array of
        the AbstractGridGeometry, not through the additional grid
        geometry.
    :cvar RADIAL_ORIGIN_POLYLINE: NKL points must be attached to the
        radial origin polyline for a grid with radial interpolation.
        BUSINESS RULE: The optional radialGridIsComplete element must be
        defined in the grid representation if geometry is attached to
        the radial origin polyline.
    :cvar SUBNODES: Geometry may be attached to subnodes to distort the
        geometry of all cells that refer to that subnode (finite element
        grid). BUSINESS RULE: An optional subnode patch object must be
        defined in the grid representation if geometry is attached to
        the subnodes.
    """

    CELLS = "cells"
    EDGES = "edges"
    FACES = "faces"
    HINGE_NODE_FACES = "hinge node faces"
    NODES = "nodes"
    RADIAL_ORIGIN_POLYLINE = "radial origin polyline"
    SUBNODES = "subnodes"


@dataclass
class HsvColor:
    """See https://en.wikipedia.org/wiki/HSL_and_HSV

    :ivar alpha: Transparency/opacity of the color: 0 is totally
        transparent while 1 is totally opaque.
    :ivar hue: Hue of the color in the HSV model.
    :ivar saturation: Saturation of the color in the HSV model.
    :ivar title: Name of the color.
    :ivar value: Value of the color in the HSV model.
    """

    alpha: Optional[float] = field(
        default=None,
        metadata={
            "name": "Alpha",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        },
    )
    hue: Optional[float] = field(
        default=None,
        metadata={
            "name": "Hue",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        },
    )
    saturation: Optional[float] = field(
        default=None,
        metadata={
            "name": "Saturation",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        },
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "name": "Title",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        },
    )
    value: Optional[float] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        },
    )


class IdentityKind(Enum):
    """
    Enumeration of the identity kinds for the element identities (ElementIdentity).

    :cvar COLLOCATION: A set of (sub)representations is collocated if
        there is bijection between the simple elements of all of the
        participating (sub)representations. This definition implies
        there is the same number of simple elements. NOTE: The geometric
        location of each set of simple elements mapped through the
        bijection is intended to be identical even if the numeric values
        of the associated geometries differ, i.e., due to loss of
        spatial resolution.
    :cvar PREVIOUS_COLLOCATION: The participating (sub)representations
        were collocated at some time in the geologic past—but not
        necessarily in the present day earth model.
    :cvar EQUIVALENCE: A set of (sub)representations is equivalent if
        there is a map giving an association between some of the simple
        topological elements of the participating (sub)representations.
    :cvar PREVIOUS_EQUIVALENCE: The participating (sub)representations
        were equivalent at some time in the geologic past—but not
        necessarily in the present day earth model.
    """

    COLLOCATION = "collocation"
    PREVIOUS_COLLOCATION = "previous collocation"
    EQUIVALENCE = "equivalence"
    PREVIOUS_EQUIVALENCE = "previous equivalence"


class InterpolationDomain(Enum):
    """
    Color domain/model for interpolation.

    :cvar HSV: Hue Saturation Value color model.
    :cvar RGB: Red Green Blue color model.
    """

    HSV = "hsv"
    RGB = "rgb"


class InterpolationMethod(Enum):
    """
    Method for interpolation.
    """

    LINEAR = "linear"
    LOGARITHMIC = "logarithmic"


class Kdirection(Enum):
    """Enumeration used to specify if the direction of the coordinate lines is
    uniquely defined for a grid.

    If not uniquely defined, e.g., for over-turned reservoirs, then
    indicate that the K direction is not monotonic.

    :cvar DOWN: K is increasing with depth, dot(tangent,gradDepth)&gt;0.
    :cvar UP: K is increasing with elevation,
        dot(tangent,gradDepth)&lt;0.
    :cvar NOT_MONOTONIC: K is not monotonic with elevation, e.g., for
        over-turned structures.
    """

    DOWN = "down"
    UP = "up"
    NOT_MONOTONIC = "not monotonic"


class LineRole(Enum):
    """
    Indicates the various roles that a polyline topology can have in a
    representation.

    :cvar FAULT_CENTER_LINE: Usually used to represent fault lineaments
        on horizons. These lines can represent nonsealed contact
        interpretation parts defined by a horizon/fault intersection.
    :cvar PICK: Used to represent several ordered points of interest on
        surfaces (commonly sections, lines or even geological surfaces)
        on which seismic is visible.
    :cvar INNER_RING: Closed polyline that delineates a hole in a
        surface patch.
    :cvar OUTER_RING: Closed polyline that delineates the extension of a
        surface patch.
    :cvar TRAJECTORY: Polyline that is used to represent a well
        trajectory representation.
    :cvar INTERPRETATION_LINE: Line corresponding to a digitalization
        along an earth model section.
    :cvar CONTACT: Used to represent nonsealed contact interpretation
        parts defined by a horizon/fault intersection.
    :cvar DEPOSITIONAL_LINE: Used to represent nonsealed contact
        interpretation parts defined by a horizon/horizon intersection.
    :cvar EROSION_LINE: Used to represent nonsealed contact
        interpretation parts defined by a horizon/horizon intersection.
    :cvar CONTOUR: Used to obtain sets of 3D x, y, z points to represent
        any boundary interpretation.
    :cvar PILLAR: Used to represent the pillars of a column-layer
        volumic grid.
    :cvar BREAK_LINE:
    :cvar STRUCTURAL_CLOSURE: A polyline representing the isobath of the
        structure's spill point
    :cvar CULTURE:
    """

    FAULT_CENTER_LINE = "fault center line"
    PICK = "pick"
    INNER_RING = "inner ring"
    OUTER_RING = "outer ring"
    TRAJECTORY = "trajectory"
    INTERPRETATION_LINE = "interpretation line"
    CONTACT = "contact"
    DEPOSITIONAL_LINE = "depositional line"
    EROSION_LINE = "erosion line"
    CONTOUR = "contour"
    PILLAR = "pillar"
    BREAK_LINE = "break line"
    STRUCTURAL_CLOSURE = "structural closure"
    CULTURE = "culture"


class MdDomain(Enum):
    """
    Different types of measured depths.

    :cvar DRILLER: The original depths recorded while drilling a well or
        LWD or MWD.
    :cvar LOGGER: Depths recorded when logging a well, which are in
        general considered to be more accurate than driller's depth.
    """

    DRILLER = "driller"
    LOGGER = "logger"


@dataclass
class MinMax:
    """
    A simple reusable structure that carries a minimum and a maximum double value
    leading to the definition of an interval of values.

    :ivar minimum: The minimum value of the interval.
    :ivar maximum: The maximum value of the interval.
    """

    minimum: Optional[float] = field(
        default=None,
        metadata={
            "name": "Minimum",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        },
    )
    maximum: Optional[float] = field(
        default=None,
        metadata={
            "name": "Maximum",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        },
    )


class NodeSymbol(Enum):
    """
    Standardized symbols for node visualization.
    """

    CIRCLE = "circle"
    CROSS = "cross"
    CUBE = "cube"
    DIAMOND = "diamond"
    PLUS = "plus"
    POINT = "point"
    PYRAMID = "pyramid"
    SPHERE = "sphere"
    STAR = "star"
    TETRAHEDRON = "tetrahedron"


class OrderingCriteria(Enum):
    """
    Enumeration used to specify the order of an abstract stratigraphic organization
    or a structural organization interpretation.

    :cvar AGE: From youngest to oldest period (increasing age).
    :cvar APPARENT_DEPTH: From surface to subsurface.
    """

    AGE = "age"
    APPARENT_DEPTH = "apparent depth"


class Phase(Enum):
    """The enumeration of the possible rock fluid unit phases in a hydrostatic
    column.

    The seal is considered here as a part (the coverage phase) of a
    hydrostatic column.

    :cvar AQUIFER: Volume of the hydrostatic column for which only the
        aqueous phase is mobile. Typically below the Pc (hydrocarbon-
        water) = 0 free fluid surface.
    :cvar GAS_CAP: Volume of the hydrostatic column for which only the
        gaseous phase is mobile. Typically above the Pc (gas-oil) = 0
        free fluid surface.
    :cvar OIL_COLUMN: Volume of the hydrostatic column for which only
        the oleic and aqueous phases may be mobile. Typically below the
        gas-oil Pc = 0 free fluid surface. Pc (gas-oil) = 0 free fluid
        surface.
    :cvar SEAL: Impermeable volume that provides the seal for a
        hydrostatic fluid column.
    """

    AQUIFER = "aquifer"
    GAS_CAP = "gas cap"
    OIL_COLUMN = "oil column"
    SEAL = "seal"


class PillarShape(Enum):
    """Used to indicate that all pillars are of a uniform kind, i.e., may be
    represented using the same number of nodes per pillar.

    This information is supplied by the RESQML writer to indicate the complexity of the grid geometry, as an aide to the RESQML reader.
    If a combination of vertical and straight, then use straight.
    If a specific pillar shape is not appropriate, then use curved.
    BUSINESS RULE: Should be consistent with the actual geometry of the grid.

    :cvar VERTICAL: If represented by a parametric line, requires only a
        single control point per line.
    :cvar STRAIGHT: If represented by a parametric line, requires 2
        control points per line.
    :cvar CURVED: If represented by a parametric line, requires 3 or
        more control points per line.
    """

    VERTICAL = "vertical"
    STRAIGHT = "straight"
    CURVED = "curved"


@dataclass
class Point3D:
    """
    Defines a point using coordinates in 3D space.

    :ivar coordinate1: X coordinate
    :ivar coordinate2: Y coordinate
    :ivar coordinate3: Either Z or T coordinate
    """

    class Meta:
        name = "Point3d"

    coordinate1: Optional[float] = field(
        default=None,
        metadata={
            "name": "Coordinate1",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        },
    )
    coordinate2: Optional[float] = field(
        default=None,
        metadata={
            "name": "Coordinate2",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        },
    )
    coordinate3: Optional[float] = field(
        default=None,
        metadata={
            "name": "Coordinate3",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        },
    )


class SequenceStratigraphySurfaceKind(Enum):
    """
    The enumerated attributes of a horizon.
    """

    FLOODING = "flooding"
    MAXIMUM_FLOODING = "maximum flooding"
    REGRESSIVE = "regressive"
    MAXIMUM_REGRESSIVE = "maximum regressive"
    TRANSGRESSIVE = "transgressive"
    MAXIMUM_TRANSGRESSIVE = "maximum transgressive"
    ABANDONMENT = "abandonment"
    CORRELATIVE_CONFORMITY = "correlative conformity"
    RAVINEMENT = "ravinement"
    SEQUENCE_BOUNDARY = "sequence boundary"


class Shape3D(Enum):
    """
    Enumeration characterizing the 3D shape of a geological unit.
    """

    SHEET = "sheet"
    DYKE = "dyke"
    DOME = "dome"
    MUSHROOM = "mushroom"
    CHANNEL = "channel"
    DELTA = "delta"
    DUNE = "dune"
    FAN = "fan"
    REEF = "reef"
    WEDGE = "wedge"


class StratigraphicRole(Enum):
    """Interpretation of the stratigraphic role of a picked horizon (chrono, litho
    or bio).

    Here the word "role" is a business term which doesn’t correspond to
    an entity dependent from an external property but simply
    characterizes a kind of horizon.
    """

    CHRONOSTRATIGRAPHIC = "chronostratigraphic"
    LITHOSTRATIGRAPHIC = "lithostratigraphic"
    BIOSTRATIGRAPHIC = "biostratigraphic"
    MAGNETOSTRATIGRAPHIC = "magnetostratigraphic"
    CHEMOSTRATIGRAPHIC = "chemostratigraphic"
    SEISMICSTRATIGRAPHIC = "seismicstratigraphic"


class StreamlineFlux(Enum):
    """
    Enumeration of the usual streamline fluxes.

    :cvar OIL: Oil Phase flux
    :cvar GAS: Gas Phase flux
    :cvar WATER: Water Phase flux
    :cvar TOTAL: Sum of (Water + Oil + Gas) Phase fluxes
    :cvar OTHER: Used to indicate that another flux is being traced.
        BUSINESS RULE: OtherFlux should appear if this value is
        specified.
    """

    OIL = "oil"
    GAS = "gas"
    WATER = "water"
    TOTAL = "total"
    OTHER = "other"


class SubnodeNodeObject(Enum):
    """SubnodeNodeObject is used to specify the node object that supports the
    subnodes.

    This determines the number of nodes per subnode and the continuity
    of the associated geometry or property. For instance, for hexahedral
    cells, cell indicates a fixed value of 8, while for an unstructured
    column layer grid, cell indicates that this count varies from column
    to column.

    :cvar CELL: If geometry or properties are discontinuous from cell to
        cell (i.e., their spatial support is cell), then attach them to
        cell subnodes. BUSINESS RULE: If this object kind is selected,
        then an ordered list of nodes per cell must be specified or
        otherwise known.
    :cvar FACE: If geometry or properties are continuous between cells
        that share the same face (i.e., their spatial support is the
        face), then attach them to face subnodes. BUSINESS RULE: If this
        object kind is selected, then an ordered list of nodes per face
        must be specified or otherwise known.
    :cvar EDGE: If geometry and properties are continuous between cells
        that share the same edge of a face (i.e. their spatial support
        is the edge), then attach them to edge subnodes. BUSINESS RULE:
        If this object kind is selected, then an ordered list of nodes
        per edge must be specified or otherwise known.
    """

    CELL = "cell"
    FACE = "face"
    EDGE = "edge"


class SurfaceRole(Enum):
    """
    Indicates the various roles that a surface topology can have.

    :cvar MAP: Representation support for properties.
    :cvar PICK: Representation support for 3D points picked in 2D or 3D.
    """

    MAP = "map"
    PICK = "pick"


class ThrowKind(Enum):
    """
    Enumeration that characterizes the type of discontinuity corresponding to a
    fault.

    :cvar REVERSE:
    :cvar STRIKE_SLIP:
    :cvar NORMAL:
    :cvar THRUST:
    :cvar SCISSOR:
    :cvar VARIABLE: Used when a throw has different behaviors during its
        lifetime.
    """

    REVERSE = "reverse"
    STRIKE_SLIP = "strike-slip"
    NORMAL = "normal"
    THRUST = "thrust"
    SCISSOR = "scissor"
    VARIABLE = "variable"


class ViewerKind(Enum):
    """
    Standardized kinds of viewers.

    :cvar VALUE_3D: A viewer where data objects are visualized in a 3D
        space.
    :cvar BASE_MAP: A viewer where data objects are visualized in 2D
        from above.
    :cvar SECTION: A viewer where data objects are laterally visualized
        in 2D.
    :cvar WELL_CORRELATION: A viewer where several well-related data
        objects (mostly channels and markers) are visualized against
        depth.
    """

    VALUE_3D = "3d"
    BASE_MAP = "base map"
    SECTION = "section"
    WELL_CORRELATION = "well correlation"


@dataclass
class AbstractColorMap(AbstractObject):
    null_color: Optional[HsvColor] = field(
        default=None,
        metadata={
            "name": "NullColor",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        },
    )
    above_max_color: Optional[HsvColor] = field(
        default=None,
        metadata={
            "name": "AboveMaxColor",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        },
    )
    below_min_color: Optional[HsvColor] = field(
        default=None,
        metadata={
            "name": "BelowMinColor",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        },
    )


@dataclass
class AbstractContactInterpretationPart:
    """The parent class of an atomic, linear, or surface geologic contact
    description.

    When the contact is between two surface representations (e.g.,
    fault/fault, horizon/fault, horizon/horizon), then the contact is a
    line. When the contact is between two volume representations
    (stratigraphic unit/stratigraphic unit), then the contact is a
    surface. A contact interpretation can be associated with other
    contact interpretations in an organization interpretation. To define
    a contact representation, you must first define a contact
    interpretation.
    """

    part_of: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "PartOf",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        },
    )


@dataclass
class AbstractFeature(AbstractObject):
    """Something that has physical existence at some point during the exploration,
    development, production or abandonment of a reservoir.

    For example: It can be a boundary, a rock volume, a basin area, but also extends to a drilled well, a drilling rig, an injected or produced fluid, or a 2D, 3D, or 4D seismic survey.
    Features are divided into these categories: geologic or technical.
    """

    is_well_known: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsWellKnown",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        },
    )


@dataclass
class AbstractFeatureInterpretation(AbstractObject):
    """
    The main class that contains all of the other feature interpretations included
    in an interpreted model.

    :ivar domain: An enumeration that specifies in which domain the
        interpretation of an AbstractFeature has been performed: depth,
        time, mixed (= depth + time )
    :ivar has_occurred_during:
    :ivar interpreted_feature:
    """

    domain: Optional[Domain] = field(
        default=None,
        metadata={
            "name": "Domain",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        },
    )
    has_occurred_during: Optional[AbstractTimeInterval] = field(
        default=None,
        metadata={
            "name": "HasOccurredDuring",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        },
    )
    interpreted_feature: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "InterpretedFeature",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        },
    )


@dataclass
class AbstractGeometry:
    """
    The base class for all geometric values, which is always associated with a
    representation.
    """

    time_index: Optional[TimeIndex] = field(
        default=None,
        metadata={
            "name": "TimeIndex",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        },
    )
    local_crs: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "LocalCrs",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        },
    )


@dataclass
class AbstractGraphicalInformationForIndexableElement:
    """
    Some general attributes for graphical information applied on some particular
    indexable elements.

    :ivar active_alpha_information_index: Index into the graphical
        information set.
    :ivar active_annotation_information_index: Index into the graphical
        information set
    :ivar active_color_information_index: Index into the graphical
        information set
    :ivar active_size_information_index: Index into the graphical
        information set
    :ivar constant_alpha: It multiplies the opacity of the color map. If
        defined, then AlphaInformation cannot be defined.
    :ivar is_visible: Indicates if this graphical information is
        intended to be visible or only stored/transferred.
    :ivar overwrite_color_alpha: If both ConstantAlpha and either
        ConstantColor or ColorInformation are defined, then setting this
        field to true will indicate that the ConstantAlpha must be used
        instead of the ConstantColor or ColorInformation alpha(s). Else
        the product of the two alpha should be used.
    :ivar constant_color:
    """

    active_alpha_information_index: Optional[int] = field(
        default=None,
        metadata={
            "name": "ActiveAlphaInformationIndex",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        },
    )
    active_annotation_information_index: Optional[int] = field(
        default=None,
        metadata={
            "name": "ActiveAnnotationInformationIndex",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        },
    )
    active_color_information_index: Optional[int] = field(
        default=None,
        metadata={
            "name": "ActiveColorInformationIndex",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        },
    )
    active_size_information_index: Optional[int] = field(
        default=None,
        metadata={
            "name": "ActiveSizeInformationIndex",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        },
    )
    constant_alpha: Optional[float] = field(
        default=None,
        metadata={
            "name": "ConstantAlpha",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        },
    )
    is_visible: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsVisible",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        },
    )
    overwrite_color_alpha: Optional[bool] = field(
        default=None,
        metadata={
            "name": "OverwriteColorAlpha",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        },
    )
    constant_color: Optional[HsvColor] = field(
        default=None,
        metadata={
            "name": "ConstantColor",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        },
    )


@dataclass
class AbstractProperty(AbstractObject):
    """Base class for storing all property values on representations, except
    current geometry location.

    Values attached to a given element can be either a scalar or a
    vector. The size of the vector is constant on all elements, and it
    is assumed that all elements of the vector have identical property
    types and share the same unit of measure.

    :ivar indexable_element:
    :ivar time:
    :ivar realization_indices: Provide the list of indices corresponding
        to realizations number. For example, if a user wants to send the
        realization corresponding to p10, p20, ... he would write the
        array 10, 20, ... If not provided, then the realization count
        (which could be 1) does not introduce a dimension to the multi-
        dimensional array storage.
    :ivar value_count_per_indexable_element: The count of value in one
        dimension for each indexable element. It is ordered as the
        values are ordered in the data set. REMINDER: First (left) given
        dimension is slowest and last (right) given dimension is
        fastest. The top XML element is slower than the bottom.
    :ivar property_kind: Pointer to a PropertyKind.  The Energistics
        dictionary can be found at
        http://w3.energistics.org/energyML/data/common/v2.1/ancillary/PropertyKindDictionary_v2.1.0.xml.
    :ivar label_per_component: Labels for each component of a vector or
        tensor property in a linearized way. REMINDER: First (left)
        given dimension is slowest and last (right) given dimension is
        fastest.
    :ivar supporting_representation:
    :ivar local_crs:
    :ivar time_or_interval_series:
    """

    indexable_element: Optional[IndexableElement] = field(
        default=None,
        metadata={
            "name": "IndexableElement",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        },
    )
    time: Optional[GeologicTime] = field(
        default=None,
        metadata={
            "name": "Time",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        },
    )
    realization_indices: Optional[AbstractIntegerArray] = field(
        default=None,
        metadata={
            "name": "RealizationIndices",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        },
    )
    value_count_per_indexable_element: List[int] = field(
        default_factory=list,
        metadata={
            "name": "ValueCountPerIndexableElement",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "min_occurs": 1,
            "min_inclusive": 1,
        },
    )
    property_kind: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "PropertyKind",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        },
    )
    label_per_component: List[str] = field(
        default_factory=list,
        metadata={
            "name": "LabelPerComponent",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "max_length": 64,
        },
    )
    supporting_representation: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "SupportingRepresentation",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        },
    )
    local_crs: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "LocalCrs",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        },
    )
    time_or_interval_series: Optional[TimeOrIntervalSeries] = field(
        default=None,
        metadata={
            "name": "TimeOrIntervalSeries",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        },
    )


@dataclass
class AbstractRepresentation(AbstractObject):
    """The parent class of all specialized digital descriptions, which may provide
    a representation of any kind of representable object such as interpretations,
    technical features, or WITSML wellbores. It may be either of these:

    - based on a topology and contains the geometry of this digital description.
    - based on the topology or the geometry of another representation.
    Not all representations require a defined geometry. For example, a defined geometry is not required for block-centered grids or wellbore frames. For representations without geometry, a software writer may provide null (NaN) values in the local 3D CRS, which is mandatory.
    TimeIndex is provided to describe time-dependent geometry.

    :ivar realization_index: Optional element indicating a realization
        id (metadata). Used if the representation is created by a
        stochastic or Monte Carlo method. Representations with the same
        id are based on the same set of random values.
    :ivar represented_object: BUSINESS RULE: The data object represented
        by the representation is either an interpretation or a technical
        feature.
    """

    realization_index: Optional[int] = field(
        default=None,
        metadata={
            "name": "RealizationIndex",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "min_inclusive": 1,
        },
    )
    represented_object: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "RepresentedObject",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        },
    )


@dataclass
class AbstractSeismicCoordinates:
    """Parent class that is used to associate horizon and fault representations to
    seismic 2D and seismic 3D technical features.

    It stores a 1-to-1 mapping between geometry coordinates (usually X,
    Y, Z) and trace or inter-trace positions on a seismic survey.
    """

    seismic_support: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "SeismicSupport",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        },
    )


@dataclass
class Activation:
    """Used to activate and deactivate the referencing object at the times
    indicated.

    - If the activation object is not present, then the referencing object is always active.
    - If the activation object is present, then the referencing object is not active until activated.

    :ivar activation_toggle_indices: The index in the time series at
        which the state of the referencing object is changed. Toggle
        changes state from inactive to active, or toggle changes state
        from active to inactive.
    :ivar time_series:
    """

    activation_toggle_indices: Optional[AbstractIntegerArray] = field(
        default=None,
        metadata={
            "name": "ActivationToggleIndices",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        },
    )
    time_series: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "TimeSeries",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        },
    )


@dataclass
class AdditionalGridPoints:
    """
    Geometry given by means of points attached to additional elements of a grid.

    :ivar representation_patch_index: Used to remove ambiguity in
        geometry attachment, if the attachment element is not
        sufficient. Usually required for subnodes and for the general
        purpose grid, but not otherwise.
    :ivar attachment:
    :ivar points:
    """

    representation_patch_index: Optional[int] = field(
        default=None,
        metadata={
            "name": "RepresentationPatchIndex",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "min_inclusive": 0,
        },
    )
    attachment: Optional[GridGeometryAttachment] = field(
        default=None,
        metadata={
            "name": "Attachment",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        },
    )
    points: Optional[AbstractPoint3DArray] = field(
        default=None,
        metadata={
            "name": "Points",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        },
    )


@dataclass
class AlphaInformation(AbstractGraphicalInformation):
    """Used for continuous properties and property kinds and for geometry.

    In the latter case, we need to point to the representation.

    :ivar alpha: Count equals to entry count. It multiplies the opacity
        of the color map.
    :ivar index: Count equals to opacity count.
    :ivar min_max:
    :ivar overwrite_color_alpha: If both Alpha and either ConstantColor
        or ColorInformation are defined, then setting this field to true
        will indicate that the Alpha must be used instead of the
        ConstantColor or ColorInformation alpha(s). Else the product of
        the two alpha should be used.
    :ivar use_logarithmic_mapping: Indicates that the log of the
        property values are taken into account when mapped with the
        index of the color map.
    :ivar use_reverse_mapping: Indicates that the minimum value of the
        property corresponds to the maximum index of the color map and
        that the maximum value of the property corresponds to the
        minimum index of the color map.
    :ivar value_vector_index: Especially useful for vector property and
        for geometry.
    """

    alpha: List[float] = field(
        default_factory=list,
        metadata={
            "name": "Alpha",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "min_occurs": 2,
        },
    )
    index: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Index",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "min_occurs": 2,
        },
    )
    min_max: Optional[MinMax] = field(
        default=None,
        metadata={
            "name": "MinMax",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        },
    )
    overwrite_color_alpha: Optional[bool] = field(
        default=None,
        metadata={
            "name": "OverwriteColorAlpha",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        },
    )
    use_logarithmic_mapping: Optional[bool] = field(
        default=None,
        metadata={
            "name": "UseLogarithmicMapping",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        },
    )
    use_reverse_mapping: Optional[bool] = field(
        default=None,
        metadata={
            "name": "UseReverseMapping",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        },
    )
    value_vector_index: Optional[int] = field(
        default=None,
        metadata={
            "name": "ValueVectorIndex",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        },
    )


@dataclass
class AlternateCellIndex:
    """Allows definition of an alternate cell indexing for a representation.

    If defined, this alternate cell indexing is the only one to rely on
    when referencing the representation cells. The alternate cell
    indices must come from existing grid representations. Because this
    alternate indexing requires a lot of extra work for software readers
    to process, use only when no other solution is acceptable.

    :ivar cell_index: Defines each alternate cell index for each
        representation cell. BUSINESS RULE :CellIndex.Count =
        GridIndex.Count = Representation.Cell.Count
    :ivar grid_index: Defines which grid each alternate cell index comes
        from. The grids are defined by means of an index of the
        OriginalGrids set. BUSINESS RULE : GridIndex.Count =
        CellIndex.Count = Representation.Cell.Count
    :ivar original_grids:
    """

    cell_index: Optional[AbstractIntegerArray] = field(
        default=None,
        metadata={
            "name": "CellIndex",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        },
    )
    grid_index: Optional[AbstractIntegerArray] = field(
        default=None,
        metadata={
            "name": "GridIndex",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        },
    )
    original_grids: List[DataObjectReference] = field(
        default_factory=list,
        metadata={
            "name": "OriginalGrids",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "min_occurs": 1,
        },
    )


@dataclass
class AnnotationInformation(AbstractGraphicalInformation):
    """Used for properties and property kinds and for geometry.

    In the latter case, we need to point to the representation.

    :ivar show_annotation_every: Shows the annotation (i.e., the value)
        on some of the indexable element on a regular basis.
    :ivar value_vector_indices: Especially useful for vector property
        and for geometry.
    """

    show_annotation_every: Optional[int] = field(
        default=None,
        metadata={
            "name": "ShowAnnotationEvery",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        },
    )
    value_vector_indices: List[str] = field(
        default_factory=list,
        metadata={
            "name": "ValueVectorIndices",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "min_occurs": 1,
        },
    )


@dataclass
class BooleanArrayFromDiscretePropertyArray(AbstractBooleanArray):
    """An array of Boolean values that is explicitly defined by indicating which
    indices in the array are either true or false.

    This class is used to represent very sparse true or false data,
    based on a discrete property.

    :ivar value: Integer to match for the value to be considered true
    :ivar property:
    """

    value: Optional[int] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        },
    )
    property: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "Property",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        },
    )


@dataclass
class BoundaryFeatureInterpretationPlusItsRank:
    """Element that lets you index and order feature interpretations which must be
    boundaries (horizon, faults and frontiers) or boundary sets (fault network).

    For possible ordering criteria, see OrderingCriteria.
    BUSINESS RULE: Only BoundaryFeatureInterpretation and FeatureInterpretationSet having faults as homogeneous type must be used to build a StructuralOrganizationInterpretation.

    :ivar stratigraphic_rank: The first rank on which you find the
        boundary or the interpretation set of boundaries.
    :ivar boundary_feature_interpretation:
    :ivar feature_interpretation_set:
    """

    stratigraphic_rank: Optional[int] = field(
        default=None,
        metadata={
            "name": "StratigraphicRank",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "min_inclusive": 0,
        },
    )
    boundary_feature_interpretation: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "BoundaryFeatureInterpretation",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        },
    )
    feature_interpretation_set: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "FeatureInterpretationSet",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        },
    )


@dataclass
class CellFluidPhaseUnits:
    """
    A mapping from cells to fluid phase unit interpretation to describe the initial
    hydrostatic fluid column.

    :ivar phase_unit_indices: Index of the phase unit kind within a
        given fluid phase organization for each cell. Follows the
        indexing defined by the PhaseUnit enumeration. When applied to
        the wellbore frame representation, the indexing is identical to
        the number of intervals. Since a single cell or interval may
        corresponds to several units, the mapping is done using a jagged
        array. Use null value if no fluid phase is present, e.g., within
        the seal. BUSINESS RULE: Array length is equal to the number of
        cells in the representation (grid, wellbore frame or blocked
        well).
    :ivar rock_fluid_organization_interpretation:
    """

    phase_unit_indices: Optional[JaggedArray] = field(
        default=None,
        metadata={
            "name": "PhaseUnitIndices",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        },
    )
    rock_fluid_organization_interpretation: Optional[
        DataObjectReference
    ] = field(
        default=None,
        metadata={
            "name": "RockFluidOrganizationInterpretation",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        },
    )


@dataclass
class ColorInformation(AbstractGraphicalInformation):
    """Used for properties and property kinds and for geometry.

    In the latter case, we need to point to the representation.

    :ivar min_max: This is the range of values of the associated
        property which will result in the minimum color and the maximum
        color. This is not necessarily the entire range of values of the
        data - data outside this range will continue to have the extreme
        color from this range.
    :ivar use_logarithmic_mapping: Indicates that the log of the
        property values are taken into account when mapped with the
        index of the color map.
    :ivar use_reverse_mapping: Indicates that the minimum value of the
        property corresponds to the maximum index of the color map and
        that the maximum value of the property corresponds to the
        minimum index of the color map.
    :ivar value_vector_index: Especially useful for vectorial property
        and for geometry.
    :ivar color_map:
    """

    min_max: Optional[MinMax] = field(
        default=None,
        metadata={
            "name": "MinMax",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        },
    )
    use_logarithmic_mapping: Optional[bool] = field(
        default=None,
        metadata={
            "name": "UseLogarithmicMapping",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        },
    )
    use_reverse_mapping: Optional[bool] = field(
        default=None,
        metadata={
            "name": "UseReverseMapping",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        },
    )
    value_vector_index: Optional[int] = field(
        default=None,
        metadata={
            "name": "ValueVectorIndex",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        },
    )
    color_map: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "ColorMap",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        },
    )


@dataclass
class ColumnLayerSplitCoordinateLines:
    """Definition of the indexing for the split coordinate lines.

    When present, this indexing contributes to the coordinate line
    nodes.

    :ivar count: Number of split coordinate lines. The count must be
        positive.
    :ivar pillar_indices: Pillar index for each split coordinate line.
        Length of this array is equal to the number of split coordinate
        lines. For the first pillarCount lines, the index of the
        coordinate line equals the index of the corresponding pillar.
        This array provides the pillar indices for the additional
        (split) coordinate lines. Used to implicitly define column and
        cell geometry.
    :ivar columns_per_split_coordinate_line: Column indices for each of
        the split coordinate lines. Used to implicitly define column and
        cell geometry. List-of-lists construction used to support shared
        coordinate lines.
    """

    count: Optional[int] = field(
        default=None,
        metadata={
            "name": "Count",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
            "min_inclusive": 1,
        },
    )
    pillar_indices: Optional[AbstractIntegerArray] = field(
        default=None,
        metadata={
            "name": "PillarIndices",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        },
    )
    columns_per_split_coordinate_line: Optional[JaggedArray] = field(
        default=None,
        metadata={
            "name": "ColumnsPerSplitCoordinateLine",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        },
    )


@dataclass
class ConnectionInterpretations:
    """For each connection in the grid connection set representation, zero, one or
    more feature-interpretations.

    The use of a jagged array allows multiple interpretations for each
    connection, e.g., to represent multiple faults discretized onto a
    single connection. Note: Feature-interpretations are not restricted
    to faults, so that a connection may also represent a horizon or
    geobody boundary, for example.

    :ivar interpretation_indices: Indices for the interpretations for
        each connection, if any. The use of a RESQML jagged array allows
        zero or more than one interpretation to be associated with a
        single connection.
    :ivar feature_interpretation:
    """

    interpretation_indices: Optional[JaggedArray] = field(
        default=None,
        metadata={
            "name": "InterpretationIndices",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        },
    )
    feature_interpretation: List[DataObjectReference] = field(
        default_factory=list,
        metadata={
            "name": "FeatureInterpretation",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "min_occurs": 1,
        },
    )


@dataclass
class ContactElement(DataObjectReference):
    """A reference to either a geologic feature interpretation or a frontier
    feature.

    BUSINESS RULE: The content type of the corresponding data-object reference must be a geological feature-interpretation or a frontier feature.
    """

    qualifier: Optional[ContactSide] = field(
        default=None,
        metadata={
            "name": "Qualifier",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        },
    )
    secondary_qualifier: Optional[ContactMode] = field(
        default=None,
        metadata={
            "name": "SecondaryQualifier",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        },
    )


@dataclass
class ContactIdentity:
    """Indicates identity between two (or more) contacts.

    For possible types of identities, see IdentityKind.

    :ivar identity_kind: The kind of contact identity. Must be one of
        the enumerations in IdentityKind.
    :ivar contact_indices: The contact representations that share common
        identity as specified by their indices.
    :ivar identical_node_indices: Indicates which nodes (identified by
        their common index in all contact representations) of the
        contact representations are identical. If this list is not
        present, then it indicates that all nodes in each representation
        are identical, on an element by element level.
    """

    identity_kind: Optional[IdentityKind] = field(
        default=None,
        metadata={
            "name": "IdentityKind",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        },
    )
    contact_indices: Optional[AbstractIntegerArray] = field(
        default=None,
        metadata={
            "name": "ContactIndices",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        },
    )
    identical_node_indices: Optional[AbstractIntegerArray] = field(
        default=None,
        metadata={
            "name": "IdenticalNodeIndices",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        },
    )


@dataclass
class ContactPatch:
    """
    A subset of topological elements of an existing contact representation part
    (sealed or non-sealed contact).

    :ivar representation_index: Identifies a representation by its
        index, in the list of representations contained in the
        organization.
    :ivar supporting_representation_nodes: The ordered list of nodes
        (identified by their global index) in the supporting
        representation, which constitutes the contact patch.
    """

    representation_index: Optional[int] = field(
        default=None,
        metadata={
            "name": "RepresentationIndex",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
            "min_inclusive": 0,
        },
    )
    supporting_representation_nodes: Optional[AbstractIntegerArray] = field(
        default=None,
        metadata={
            "name": "SupportingRepresentationNodes",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        },
    )


@dataclass
class ContactReference(AbstractSurfaceFrameworkContact):
    """
    Used when the contact already exists as a top-level element representation.
    """

    representation: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "Representation",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        },
    )


@dataclass
class ContinuousColorMapEntry:
    """
    An association between a single double value and a color.

    :ivar index: The double value to be associated with a particular
        color.
    :ivar hsv:
    """

    index: Optional[float] = field(
        default=None,
        metadata={
            "name": "Index",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        },
    )
    hsv: Optional[HsvColor] = field(
        default=None,
        metadata={
            "name": "Hsv",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        },
    )


@dataclass
class CulturalFeatureKindExt:
    value: Union[CulturalFeatureKind, str] = field(
        default="",
        metadata={
            "pattern": r".*:.*",
        },
    )


@dataclass
class DepositionalEnvironmentKindExt:
    value: Union[DepositionalEnvironmentKind, str] = field(
        default="",
        metadata={
            "pattern": r".*:.*",
        },
    )


@dataclass
class DepositionalFaciesKindExt:
    value: Union[DepositionalFaciesKind, str] = field(
        default="",
        metadata={
            "pattern": r".*:.*",
        },
    )


@dataclass
class DiscreteColorMapEntry:
    """
    An association between a single integer value and a color.

    :ivar index: The integer value to be associated with a particular
        color.
    :ivar hsv:
    """

    index: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        },
    )
    hsv: Optional[HsvColor] = field(
        default=None,
        metadata={
            "name": "Hsv",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        },
    )


@dataclass
class EdgePatch:
    """Describes edges that are not linked to any other edge.

    Because edges do not have indices, a consecutive pair of nodes is
    used to identify each edge. The split edges dataset is a set of
    nodes (2 nodes per edge). Each patch has a set of 2 nodes.

    :ivar split_edges: An array of split edges to define patches. It
        points to an HDF5 dataset, which must be a 2D array of non-
        negative integers with dimensions 2 x numSplitEdges.
    """

    split_edges: Optional[AbstractIntegerArray] = field(
        default=None,
        metadata={
            "name": "SplitEdges",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        },
    )


@dataclass
class EdgePatternExt:
    """
    Allows the use of custom edge pattern in addition to the EdgePattern
    enumeration.
    """

    value: Union[EdgePattern, str] = field(
        default="",
        metadata={
            "pattern": r".*:.*",
        },
    )


@dataclass
class Edges:
    """Unstructured cell grids require the definition of edges if the subnode
    attachment is of kind edges.

    Use Case: Finite elements, especially for higher order geometry.
    BUSINESS RULE: Edges must be defined for unstructured cell grids if subnode nodes of kind edges are used.

    :ivar count: Number of edges. Must be positive.
    :ivar nodes_per_edge: Defines a list of 2 nodes per edge. Count = 2
        x EdgeCount
    """

    count: Optional[int] = field(
        default=None,
        metadata={
            "name": "Count",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
            "min_inclusive": 1,
        },
    )
    nodes_per_edge: Optional[AbstractIntegerArray] = field(
        default=None,
        metadata={
            "name": "NodesPerEdge",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        },
    )


@dataclass
class ElementIdentity:
    """Indicates the nature of the relationship between 2 or more representations,
    specifically if they are partially or totally identical.

    For possible types of relationships, see IdentityKind. Commonly used
    to identify contacts between representations in model descriptions.
    May also be used to relate the components of a grid (e.g., pillars)
    to those of a structural framework.

    :ivar element_indices: Indicates which elements are identical based
        on their indices in the (sub)representation. If not given, then
        the selected indexable elements of each of the selected
        representations are identical at the element by element level.
        BUSINESS RULE: The number of identical elements must be equal to
        identicalElementCount for each representation.
    :ivar identity_kind: Must be one of the enumerations in
        IdentityKind.
    :ivar indexable_element:
    :ivar from_time_index:
    :ivar representation:
    :ivar to_time_index:
    """

    element_indices: Optional[AbstractIntegerArray] = field(
        default=None,
        metadata={
            "name": "ElementIndices",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        },
    )
    identity_kind: Optional[IdentityKind] = field(
        default=None,
        metadata={
            "name": "IdentityKind",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        },
    )
    indexable_element: Optional[IndexableElement] = field(
        default=None,
        metadata={
            "name": "IndexableElement",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        },
    )
    from_time_index: Optional[TimeIndex] = field(
        default=None,
        metadata={
            "name": "FromTimeIndex",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        },
    )
    representation: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "Representation",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        },
    )
    to_time_index: Optional[TimeIndex] = field(
        default=None,
        metadata={
            "name": "ToTimeIndex",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        },
    )


@dataclass
class ElementIndices:
    """
    Index into the indexable elements selected.
    """

    supporting_representation_index: Optional[AbstractIntegerArray] = field(
        default=None,
        metadata={
            "name": "SupportingRepresentationIndex",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        },
    )


@dataclass
class FaultThrow:
    """
    Identifies the characteristic of the throw of a fault interpretation.
    """

    throw: List[Union[ThrowKind, str]] = field(
        default_factory=list,
        metadata={
            "name": "Throw",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "min_occurs": 1,
            "pattern": r".*:.*",
        },
    )
    has_occurred_during: Optional[AbstractTimeInterval] = field(
        default=None,
        metadata={
            "name": "HasOccurredDuring",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        },
    )


@dataclass
class GeneticBoundaryBasedTimeInterval(AbstractTimeInterval):
    """
    Geological time during which a geological event (e.g., deposition, erosion,
    fracturation, faulting, intrusion) occurred.
    """

    chrono_bottom: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "ChronoBottom",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        },
    )
    chrono_top: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "ChronoTop",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        },
    )


@dataclass
class GeologicTimeBasedTimeInterval(AbstractTimeInterval):
    """A time interval that is bounded by two geologic times.

    Can correspond to a TimeStep in a TimeSeries, such as the
    International Chronostratigraphic Scale or a regional
    chronostratigraphic scale.
    """

    start: Optional[GeologicTime] = field(
        default=None,
        metadata={
            "name": "Start",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        },
    )
    end: Optional[GeologicTime] = field(
        default=None,
        metadata={
            "name": "End",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        },
    )


@dataclass
class IjGaps:
    """Optional object used to indicate that adjacent columns of the model are
    split from each other, which is modeled by introducing additional (split)
    pillars.

    Use the ColumnLayerSplitColumnEdges object to specify the numbering
    of the additional column edges generated by the IJ Gaps.

    :ivar split_pillar_count: Number of split pillars in the model.
        Count must be positive.
    :ivar parent_pillar_indices: Parent pillar index for each of the
        split pillars. This information is used to infer the grid cell
        geometry. BUSINESS RULE: Array length must match
        splitPillarCount.
    :ivar columns_per_split_pillar: List of columns for each of the
        split pillars. This information is used to infer the grid cell
        geometry. BUSINESS RULE: The length of the first list-of-lists
        array must match the splitPillarCount.
    """

    split_pillar_count: Optional[int] = field(
        default=None,
        metadata={
            "name": "SplitPillarCount",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
            "min_inclusive": 1,
        },
    )
    parent_pillar_indices: Optional[AbstractIntegerArray] = field(
        default=None,
        metadata={
            "name": "ParentPillarIndices",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        },
    )
    columns_per_split_pillar: Optional[JaggedArray] = field(
        default=None,
        metadata={
            "name": "ColumnsPerSplitPillar",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        },
    )


@dataclass
class IntervalGridCells:
    """Specifies the (Grid,Cell) intersection of each interval of the
    representation, if any.

    The information allows you to locate, on one or several grids, the
    intersection of volume (cells) and surface (faces) elements with a
    wellbore trajectory (existing or planned), streamline trajectories,
    or any polyline set.

    :ivar cell_count: The number of non-null entries in the grid indices
        array.
    :ivar grid_indices: The grid index for each interval of a
        representation. The grid index is specified by grid index array,
        to give the (Grid,Cell) index pair. Null values signify that the
        interval is not within a grid. BUSINESS RULE : Size of array =
        IntervalCount
    :ivar cell_indices: The cell index for each interval of a
        representation. The grid index is specified by grid index array,
        to give the (Grid,Cell) index pair. Null values signify that
        interval is not within a grid. BUSINESS RULE : Size of array =
        IntervalCount
    :ivar local_face_pair_per_cell_indices: For each cell, these are the
        entry and exit intersection faces of the trajectory in the cell.
        Use null for missing intersections, e.g., when a trajectory
        originates or terminates within a cell or when an interval is
        not within a grid. The local face-per-cell index is used because
        a global face index need not have been defined on the grid.
        BUSINESS RULE: Size of array = 2 * IntervalCount
    :ivar grid:
    """

    cell_count: Optional[int] = field(
        default=None,
        metadata={
            "name": "CellCount",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
            "min_inclusive": 1,
        },
    )
    grid_indices: Optional[AbstractIntegerArray] = field(
        default=None,
        metadata={
            "name": "GridIndices",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        },
    )
    cell_indices: Optional[AbstractIntegerArray] = field(
        default=None,
        metadata={
            "name": "CellIndices",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        },
    )
    local_face_pair_per_cell_indices: Optional[AbstractIntegerArray] = field(
        default=None,
        metadata={
            "name": "LocalFacePairPerCellIndices",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        },
    )
    grid: List[DataObjectReference] = field(
        default_factory=list,
        metadata={
            "name": "Grid",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "min_occurs": 1,
        },
    )


@dataclass
class IntervalStratigraphicUnits:
    """A mapping from intervals to stratigraphic units for representations (grids
    or wellbore frames).

    Since a single interval may corresponds to several units, the
    mapping is done using a jagged array.

    :ivar unit_indices: Index of the stratigraphic unit per interval, of
        a given stratigraphic column. Notes: 1.) For grids: if it does
        not exist a property kind "geologic k" attached to the grid then
        intervals = layers + K gaps else intervals = values property of
        property kind "geologic k" 2.) If there is no stratigraphic
        column, e.g., within salt, use null value BUSINESS RULE: Array
        length must equal the number of intervals.
    :ivar stratigraphic_organization_interpretation:
    """

    unit_indices: Optional[JaggedArray] = field(
        default=None,
        metadata={
            "name": "UnitIndices",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        },
    )
    stratigraphic_organization_interpretation: Optional[
        DataObjectReference
    ] = field(
        default=None,
        metadata={
            "name": "StratigraphicOrganizationInterpretation",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        },
    )


@dataclass
class Intervals:
    """Refinement and/or coarsening per interval.

    If there is a 1:1 correspondence between the parent and child cells,
    then this object is not needed.

    :ivar child_cell_weights: Weights that are proportional to the
        relative sizes of child cells within each interval. The weights
        need not be normalized.
    :ivar child_count_per_interval: The number of child cells in each
        interval. If the child grid type is not commensurate with the
        parent type, then this attribute is ignored by a reader and its
        value should be set to null value. For example, for a parent IJK
        grid with a child unstructured column-layer grid, then the child
        count is non-null for a K regrid, but null for an I or J regrid.
        BUSINESS RULES: 1.) The array length must be equal to
        intervalCount. 2.) If the child grid type is commensurate with
        the parent grid, then the sum of values over all intervals must
        be equal to the corresponding child grid dimension.
    :ivar interval_count: The number of intervals in the regrid
        description. Must be positive.
    :ivar parent_count_per_interval: The number of parent cells in each
        interval. BUSINESS RULES: 1.) The array length must be equal to
        intervalCount. 2.) For the given parentIndex, the total count of
        parent cells should not extend beyond the boundary of the parent
        grid.
    """

    child_cell_weights: Optional[AbstractFloatingPointArray] = field(
        default=None,
        metadata={
            "name": "ChildCellWeights",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        },
    )
    child_count_per_interval: Optional[AbstractIntegerArray] = field(
        default=None,
        metadata={
            "name": "ChildCountPerInterval",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        },
    )
    interval_count: Optional[int] = field(
        default=None,
        metadata={
            "name": "IntervalCount",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
            "min_inclusive": 1,
        },
    )
    parent_count_per_interval: Optional[AbstractIntegerArray] = field(
        default=None,
        metadata={
            "name": "ParentCountPerInterval",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        },
    )


@dataclass
class Kgaps:
    """Optional data-object used to indicate that there are global gaps between
    layers in the grid.

    With K gaps, the bottom of one layer need not be continuous with the
    top of the next layer, so the resulting number of intervals is
    greater than the number of layers.

    :ivar count: Number of gaps between layers. Must be positive. Number
        of intervals = gapCount + NK.
    :ivar gap_after_layer: Boolean array of length NK-1. TRUE if there
        is a gap after the corresponding layer. NKL = NK + gapCount + 1
        BUSINESS RULE: gapCount must be consistent with the number of
        gaps specified by the gapAfterLayer array.
    """

    class Meta:
        name = "KGaps"

    count: Optional[int] = field(
        default=None,
        metadata={
            "name": "Count",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
            "min_inclusive": 1,
        },
    )
    gap_after_layer: Optional[AbstractBooleanArray] = field(
        default=None,
        metadata={
            "name": "GapAfterLayer",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        },
    )


@dataclass
class LineRoleExt:
    value: Union[LineRole, str] = field(
        default="",
        metadata={
            "pattern": r".*:.*",
        },
    )


@dataclass
class MarkerBoundary:
    """
    Represent interval limits associated with Witsml:WellMarkers.

    :ivar fluid_contact:
    :ivar fluid_marker:
    :ivar geologic_boundary_kind:
    :ivar qualifier:
    :ivar marker_set: This is a DataObjectReference to a WITSML
        WellboreMarkerSet
    :ivar marker: This is a DataObjectReference to a WITSML
        WellboreMarker
    :ivar interpretation:
    """

    fluid_contact: Optional[FluidContact] = field(
        default=None,
        metadata={
            "name": "FluidContact",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        },
    )
    fluid_marker: Optional[FluidMarker] = field(
        default=None,
        metadata={
            "name": "FluidMarker",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        },
    )
    geologic_boundary_kind: Optional[GeologicBoundaryKind] = field(
        default=None,
        metadata={
            "name": "GeologicBoundaryKind",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        },
    )
    qualifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "Qualifier",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        },
    )
    marker_set: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "MarkerSet",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        },
    )
    marker: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "Marker",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        },
    )
    interpretation: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "Interpretation",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        },
    )


@dataclass
class MarkerInterval:
    organization: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "Organization",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        },
    )
    interpretation: List[DataObjectReference] = field(
        default_factory=list,
        metadata={
            "name": "Interpretation",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        },
    )


@dataclass
class NodeSymbolExt:
    """
    Allows you to use custom node symbols in addition to the NodeSymbol
    enumeration.
    """

    value: Union[NodeSymbol, str] = field(
        default="",
        metadata={
            "pattern": r".*:.*",
        },
    )


@dataclass
class OverlapVolume:
    """Optional parent-child cell overlap volume information.

    If not present, then the CellOverlap data-object lists the overlaps,
    but with no additional information.

    :ivar overlap_volumes: Parent-child cell volume overlap. BUSINESS
        RULE: Length of array must equal the cell overlap count.
    :ivar volume_uom: Units of measure for the overlapVolume.
    """

    overlap_volumes: Optional[AbstractFloatingPointArray] = field(
        default=None,
        metadata={
            "name": "OverlapVolumes",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        },
    )
    volume_uom: Optional[VolumeUom] = field(
        default=None,
        metadata={
            "name": "VolumeUom",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        },
    )


@dataclass
class ParametricLineFromRepresentationLatticeArray(
    AbstractParametricLineArray
):
    """The lattice array of parametric lines extracted from an existing
    representation.

    BUSINESS RULE: The supporting representation must have pillars or lines as indexable elements.

    :ivar line_indices_on_supporting_representation: The line indices of
        the selected lines in the supporting representation. The index
        selection is regularly incremented from one node to the next
        node. BUSINESS RULE: The dimensions of the integer lattice array
        must be consistent with the dimensions of the supporting
        representation. For a column-layer grid, the parametric lines
        follow the indexing of the pillars. BUSINESS RULE: The start
        value of the integer lattice array must be the linearized index
        of the starting line. Example: iStart + ni * jStart in case of a
        supporting 2D grid.
    :ivar supporting_representation:
    """

    line_indices_on_supporting_representation: Optional[
        IntegerLatticeArray
    ] = field(
        default=None,
        metadata={
            "name": "LineIndicesOnSupportingRepresentation",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        },
    )
    supporting_representation: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "SupportingRepresentation",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        },
    )


@dataclass
class ParametricLineIntersections:
    """Used to specify the intersections between parametric lines.

    This information is purely geometric and is not required for the
    evaluation of the parametric point locations on these lines. The
    information required for that purpose is stored in the parametric
    points array.

    :ivar count: Number of parametric line intersections. Must be
        positive.
    :ivar intersection_line_pairs: Intersected line index pair for (line
        1, line 2). Size = 2 x count
    :ivar parameter_value_pairs: Intersected line parameter value pairs
        for (line 1, line 2). Size = 2 x count
    """

    count: Optional[int] = field(
        default=None,
        metadata={
            "name": "Count",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
            "min_inclusive": 1,
        },
    )
    intersection_line_pairs: Optional[AbstractIntegerArray] = field(
        default=None,
        metadata={
            "name": "IntersectionLinePairs",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        },
    )
    parameter_value_pairs: Optional[AbstractValueArray] = field(
        default=None,
        metadata={
            "name": "ParameterValuePairs",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        },
    )


@dataclass
class PatchBoundaries:
    """Defines the boundaries of an indexed patch.

    These boundaries are outer and inner rings.

    :ivar referenced_patch: The XML index of the referenced patch inside
        this representation.
    :ivar inner_ring:
    :ivar outer_ring:
    """

    referenced_patch: Optional[int] = field(
        default=None,
        metadata={
            "name": "ReferencedPatch",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
            "min_inclusive": 0,
        },
    )
    inner_ring: List[DataObjectReference] = field(
        default_factory=list,
        metadata={
            "name": "InnerRing",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        },
    )
    outer_ring: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "OuterRing",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        },
    )


@dataclass
class Point2DExternalArray(AbstractPoint3DArray):
    """An array of explicit XY points stored as two coordinates in an HDF5 dataset.

    If needed, the implied Z coordinate is uniformly 0.

    :ivar coordinates: Reference to an HDF5 2D dataset of XY points. The
        2 coordinates are stored sequentially in HDF5, i.e., a multi-
        dimensional array of points is stored as a 2 x ... HDF5 array.
    """

    class Meta:
        name = "Point2dExternalArray"

    coordinates: Optional[ExternalDataArray] = field(
        default=None,
        metadata={
            "name": "Coordinates",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        },
    )


@dataclass
class Point3DExternalArray(AbstractPoint3DArray):
    """
    An array of explicit XYZ points stored as three coordinates in an HDF5 dataset.

    :ivar coordinates: Reference to an HDF5 3D dataset of XYZ points.
        The 3 coordinates are stored sequentially in HDF5, i.e., a
        multi-dimensional array of points is stored as a 3 x ... HDF5
        array.
    """

    class Meta:
        name = "Point3dExternalArray"

    coordinates: Optional[ExternalDataArray] = field(
        default=None,
        metadata={
            "name": "Coordinates",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        },
    )


@dataclass
class Point3DFromRepresentationLatticeArray(AbstractPoint3DArray):
    """A lattice array of points extracted from an existing representation.

    BUSINESS RULE: The supporting representation must have nodes as indexable elements.

    :ivar node_indices_on_supporting_representation: The node indices of
        the selected nodes in the supporting representation. The index
        selection is regularly incremented from one node to the next
        node. BUSINESS RULE: The node indices must be consistent with
        the size of supporting representation.
    :ivar supporting_representation:
    """

    class Meta:
        name = "Point3dFromRepresentationLatticeArray"

    node_indices_on_supporting_representation: Optional[
        IntegerLatticeArray
    ] = field(
        default=None,
        metadata={
            "name": "NodeIndicesOnSupportingRepresentation",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        },
    )
    supporting_representation: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "SupportingRepresentation",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        },
    )


@dataclass
class Point3DLatticeDimension:
    """Defines the size and sampling in each dimension (direction) of the point 3D
    lattice array.

    Sampling can be uniform or irregular.

    :ivar direction: The direction of the axis of this lattice
        dimension. This is a relative offset vector instead of an
        absolute 3D point.
    :ivar spacing: A lattice of N offset points is described by a
        spacing array of size N-1. The offset between points is given by
        the spacing value multiplied by the offset vector. For example,
        the first offset is 0. The second offset is the first spacing *
        offset. The second offset is (first spacing + second spacing) *
        offset, etc.
    """

    class Meta:
        name = "Point3dLatticeDimension"

    direction: Optional[Point3D] = field(
        default=None,
        metadata={
            "name": "Direction",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        },
    )
    spacing: Optional[AbstractFloatingPointArray] = field(
        default=None,
        metadata={
            "name": "Spacing",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        },
    )


@dataclass
class Point3DParametricArray(AbstractPoint3DArray):
    """
    A parametric specification of an array of XYZ points.

    :ivar parameters: A multi-dimensional array of parametric values
        that implicitly specifies an array of XYZ points. The parametric
        values provided in this data-object must be consistent with the
        parametric values specified in the referenced parametric line
        array. When constructing a column-layer grid geometry using
        parametric points, the array indexing follows the dimensionality
        of the coordinate lines x NKL, which is either a 2D or 3D array.
    :ivar parametric_line_indices: An optional array of indices that map
        from the array index to the index of the corresponding
        parametric line. If this information is known from context, then
        this array is not needed. For example, in either of these cases:
        (1) If the mapping from array index to parametric line is 1:1.
        (2) If the mapping has already been specified, as with the
        pillar Index from the column-layer geometry of a grid. For
        example, when constructing a column-layer grid geometry using
        parametric lines, the array indexing follows the dimensionality
        of the coordinate lines.
    :ivar truncated_line_indices: A 2D array of line indices for use
        with intersecting parametric lines. Each record consists of a
        single line index, which indicates the array line that uses this
        truncation information, followed by the parametric line indices
        for each of the points on that line. For a non-truncated line,
        the equivalent record repeats the array line index NKL+1 times.
        Size = (NKL+1) x truncatedLineCount
    :ivar parametric_lines:
    """

    class Meta:
        name = "Point3dParametricArray"

    parameters: Optional[AbstractValueArray] = field(
        default=None,
        metadata={
            "name": "Parameters",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        },
    )
    parametric_line_indices: Optional[AbstractIntegerArray] = field(
        default=None,
        metadata={
            "name": "ParametricLineIndices",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        },
    )
    truncated_line_indices: Optional[AbstractIntegerArray] = field(
        default=None,
        metadata={
            "name": "TruncatedLineIndices",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        },
    )
    parametric_lines: Optional[AbstractParametricLineArray] = field(
        default=None,
        metadata={
            "name": "ParametricLines",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        },
    )


@dataclass
class Point3DZvalueArray(AbstractPoint3DArray):
    """An array of points defined by applying a Z value on top of an existing array
    of points, XYZ, where Z is ignored. Used in these cases:

    - in 2D for defining geometry of one patch of a 2D grid representation.
    - for extracting nodal geometry from one grid representation for use in another.

    :ivar supporting_geometry: Geometry defining the X and Y
        coordinates.
    :ivar zvalues: The values for Z coordinates
    """

    class Meta:
        name = "Point3dZValueArray"

    supporting_geometry: Optional[AbstractPoint3DArray] = field(
        default=None,
        metadata={
            "name": "SupportingGeometry",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        },
    )
    zvalues: Optional[AbstractFloatingPointArray] = field(
        default=None,
        metadata={
            "name": "ZValues",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        },
    )


@dataclass
class SequenceStratigraphySurfaceKindExt:
    value: Union[SequenceStratigraphySurfaceKind, str] = field(
        default="",
        metadata={
            "pattern": r".*:.*",
        },
    )


@dataclass
class Shape3DExt:
    class Meta:
        name = "Shape3dExt"

    value: Union[Shape3D, str] = field(
        default="",
        metadata={
            "pattern": r".*:.*",
        },
    )


@dataclass
class SizeInformation(AbstractGraphicalInformation):
    """Used for properties and property kinds and for geometry.

    In the latter case, we need to point to the representation.

    :ivar min_max:
    :ivar use_logarithmic_mapping: Indicates that the log of the
        property values are taken into account when mapped with the
        index of the color map.
    :ivar use_reverse_mapping: Indicates that the minimum value of the
        property corresponds to the maximum index of the color map and
        that te maximum value of the property corresponds to the minimum
        index of the color map.
    :ivar value_vector_index: Especially useful for vectorial property
        and for geometry.
    """

    min_max: Optional[MinMax] = field(
        default=None,
        metadata={
            "name": "MinMax",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        },
    )
    use_logarithmic_mapping: Optional[bool] = field(
        default=None,
        metadata={
            "name": "UseLogarithmicMapping",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        },
    )
    use_reverse_mapping: Optional[bool] = field(
        default=None,
        metadata={
            "name": "UseReverseMapping",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        },
    )
    value_vector_index: Optional[int] = field(
        default=None,
        metadata={
            "name": "ValueVectorIndex",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        },
    )


@dataclass
class SplitColumnEdges:
    """Column edges are needed to construct the indices for the cell faces for
    column-layer grids.

    For split column-layer grids, the column edge indices must be
    defined explicitly. Column edges are not required to describe the
    lowest order grid geometry, but may be required for higher order
    geometries or properties.

    :ivar count: Number of split column edges in this grid. Must be
        positive.
    :ivar parent_column_edge_indices: Parent unsplit column edge index
        for each of the split column edges. Used to implicitly define
        split face indexing.
    :ivar column_per_split_column_edge: Column index for each of the
        split column edges. Used to implicitly define column and cell
        faces. List-of-lists construction not required because each
        split column edge must be in a single column.
    """

    count: Optional[int] = field(
        default=None,
        metadata={
            "name": "Count",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
            "min_inclusive": 1,
        },
    )
    parent_column_edge_indices: Optional[AbstractIntegerArray] = field(
        default=None,
        metadata={
            "name": "ParentColumnEdgeIndices",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        },
    )
    column_per_split_column_edge: Optional[AbstractIntegerArray] = field(
        default=None,
        metadata={
            "name": "ColumnPerSplitColumnEdge",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        },
    )


@dataclass
class SplitEdges:
    """If split nodes are used in the construction of a column-layer grid and
    indexable elements of kind edges are referenced, then the grid edges need to be
    re-defined.

    Use Case: finite elements, especially for higher order geometry.

    :ivar count: Number of edges. Must be positive.
    :ivar parent_edge_indices: Parent unsplit edge index for each of the
        additional split edges.
    :ivar faces_per_split_edge: Association of faces with the split
        edges, used to infer continuity of property, geometry, or
        interpretation with an attachment kind of edges.
    """

    count: Optional[int] = field(
        default=None,
        metadata={
            "name": "Count",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
            "min_inclusive": 1,
        },
    )
    parent_edge_indices: Optional[AbstractIntegerArray] = field(
        default=None,
        metadata={
            "name": "ParentEdgeIndices",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        },
    )
    faces_per_split_edge: Optional[JaggedArray] = field(
        default=None,
        metadata={
            "name": "FacesPerSplitEdge",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        },
    )


@dataclass
class StratigraphicColumn(AbstractObject):
    """A global interpretation of the stratigraphy, which can be made up of several
    ranks of stratigraphic unit interpretations.

    BUSINESS RULE: All stratigraphic column rank interpretations that make up a stratigraphic column must be ordered by age.
    """

    class Meta:
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"

    ranks: List[DataObjectReference] = field(
        default_factory=list,
        metadata={
            "name": "Ranks",
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass
class StreamlineFluxExt:
    value: Union[StreamlineFlux, str] = field(
        default="",
        metadata={
            "pattern": r".*:.*",
        },
    )


@dataclass
class StreamlineWellbores:
    """Used to specify the wellbores on which streamlines may originate or
    terminate.

    Additional properties, e.g., MD, or cell index may be used to
    specify locations along a wellbore. The 0-based wellbore index is
    defined by the order of the wellbore in the list of
    WellboreTrajectoryRepresentation references.

    :ivar injector_per_line: Size of array = LineCount. Null values
        signify that that line does not initiate at an injector, e.g.,
        it may come from fluid expansion or an aquifer.
    :ivar producer_per_line: Size of array = LineCount Null values
        signify that that line does not terminate at a producer, e.g.,
        it may approach a stagnation area. BUSINESS RULE: The cell count
        must equal the number of non-null entries in this array.
    :ivar wellbore_trajectory_representation:
    """

    injector_per_line: Optional[AbstractIntegerArray] = field(
        default=None,
        metadata={
            "name": "InjectorPerLine",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        },
    )
    producer_per_line: Optional[AbstractIntegerArray] = field(
        default=None,
        metadata={
            "name": "ProducerPerLine",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        },
    )
    wellbore_trajectory_representation: List[DataObjectReference] = field(
        default_factory=list,
        metadata={
            "name": "WellboreTrajectoryRepresentation",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "min_occurs": 1,
        },
    )


@dataclass
class SubRepresentationPatch:
    """Each sub-representation patch has its own list of representation indices,
    drawn from the supporting representation.

    If a list of pairwise elements is required, use two ElementIndices.
    The count of elements (or pair of elements) is defined in
    SubRepresentationPatch.
    """

    indices: Optional[AbstractIntegerArray] = field(
        default=None,
        metadata={
            "name": "Indices",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        },
    )
    supporting_representation: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "SupportingRepresentation",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        },
    )


@dataclass
class SubnodePatch:
    """Each patch of subnodes is defined independently of the others.

    Number of nodes per object is determined by the subnode kind.

    :ivar subnode_node_object:
    :ivar node_weights_per_subnode: Node weights for each subnode. Count
        of nodes per subnode is known for each specific subnode
        construction. Data order consists of all the nodes for each
        subnode in turn. For example, if uniform and stored as a multi-
        dimensional array, the node index cycles first. BUSINESS RULE:
        Weights must be non-negative. BUSINESS RULE: Length of array
        must be consistent with the sum of nodeCount x subnodeCount per
        object, e.g., for 3 subnodes per edge (uniform), there are 6
        weights.
    """

    subnode_node_object: Optional[SubnodeNodeObject] = field(
        default=None,
        metadata={
            "name": "SubnodeNodeObject",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        },
    )
    node_weights_per_subnode: Optional[AbstractValueArray] = field(
        default=None,
        metadata={
            "name": "NodeWeightsPerSubnode",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        },
    )


@dataclass
class ThreePoint3D:
    """
    List of three 3D points.
    """

    class Meta:
        name = "ThreePoint3d"

    point3d: List[Point3D] = field(
        default_factory=list,
        metadata={
            "name": "Point3d",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "min_occurs": 3,
            "max_occurs": 3,
        },
    )


@dataclass
class ThrowKindExt:
    value: Union[ThrowKind, str] = field(
        default="",
        metadata={
            "pattern": r".*:.*",
        },
    )


@dataclass
class TruncationCellPatch:
    """Truncation definitions for the truncated and split cells.

    BUSINESS RULE: Patch Index must be positive because a patch index of 0 refers to the fundamental column-layer coordinate line nodes and cells.

    :ivar local_faces_per_cell: Local cell face index for those faces
        that are retained from the parent cell in the definition of the
        truncation cell. The use of a local cell-face index, e.g., 0...5
        for an IJK cell, can be used even if the face indices have not
        been defined.
    :ivar nodes_per_truncation_face: Definition of the truncation faces
        is in terms of an ordered list of nodes. Node indexing is
        EXTENDED, i.e., is based on the list of untruncated grid nodes
        (always first) plus the split nodes (if any) and the truncation
        face nodes. Relative order of split nodes and truncation face
        nodes is set by the pillar indices.
    :ivar parent_cell_indices: Parent cell index for each of the
        truncation cells. BUSINESS RULE: Size must match
        truncationCellCount
    :ivar truncation_cell_count: Number of polyhedral cells created by
        truncation. Must be positive. Note: Parent cells are replaced.
    :ivar truncation_cell_face_is_right_handed: Boolean mask used to
        indicate which truncation cell faces have an outwardly directed
        normal, following a right hand rule. Data size and order follows
        the truncationFacesPerCell list-of-lists.
    :ivar truncation_face_count: Number of additional faces required for
        the split and truncation construction. The construction does not
        modify existing face definitions, but instead uses these new
        faces to redefine the truncated cell geometry. Must be positive.
        These faces are added to the enumeration of faces for the grid
    :ivar truncation_faces_per_cell: Truncation face index for the
        additional cell faces that are required to complete the
        definition of the truncation cell. The resulting local cell face
        index follows the local faces-per-cell list, followed by the
        truncation faces in the order within the list-of-lists
        constructions.
    :ivar truncation_node_count: Number of additional nodes required for
        the truncation construction. Must be positive. Uses a separate
        enumeration and does not increase the number of nodes, except as
        noted below.
    """

    local_faces_per_cell: Optional[JaggedArray] = field(
        default=None,
        metadata={
            "name": "LocalFacesPerCell",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        },
    )
    nodes_per_truncation_face: Optional[JaggedArray] = field(
        default=None,
        metadata={
            "name": "NodesPerTruncationFace",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        },
    )
    parent_cell_indices: Optional[AbstractIntegerArray] = field(
        default=None,
        metadata={
            "name": "ParentCellIndices",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        },
    )
    truncation_cell_count: Optional[int] = field(
        default=None,
        metadata={
            "name": "TruncationCellCount",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
            "min_inclusive": 1,
        },
    )
    truncation_cell_face_is_right_handed: Optional[
        AbstractBooleanArray
    ] = field(
        default=None,
        metadata={
            "name": "TruncationCellFaceIsRightHanded",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        },
    )
    truncation_face_count: Optional[int] = field(
        default=None,
        metadata={
            "name": "TruncationFaceCount",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
            "min_inclusive": 1,
        },
    )
    truncation_faces_per_cell: Optional[JaggedArray] = field(
        default=None,
        metadata={
            "name": "TruncationFacesPerCell",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        },
    )
    truncation_node_count: Optional[int] = field(
        default=None,
        metadata={
            "name": "TruncationNodeCount",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
            "min_inclusive": 1,
        },
    )


@dataclass
class TvdInformation:
    """Business rule:

    :ivar node_tvd_values: Count must be equal to count of nodes of the
        associated wellbore frame. The direction of the supporting axis
        is given by the LocalDepth3dCrs itself. It is necessary to get
        the information to know what are positive or negative values.
        The values are given with respect to the TvdDatum, not with
        respect to the ZOffest of the LocalDepth3dCrs The UOM is the one
        specified in the LocalDepth3dCrs.
    :ivar tvd_datum: The direction of the supporting axis is given by
        the LocalDepth3dCrs itself. It is necessary to get the
        information to know what is a positive or a negative value. The
        value is given with respect to the ZOffset of the
        LocalDepth3dCrs. The UOM is the one specified in the
        LocalDepth3dCrs.
    :ivar tvd_reference:
    :ivar local_depth3d_crs:
    """

    node_tvd_values: Optional[AbstractFloatingPointArray] = field(
        default=None,
        metadata={
            "name": "NodeTvdValues",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        },
    )
    tvd_datum: Optional[float] = field(
        default=None,
        metadata={
            "name": "TvdDatum",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        },
    )
    tvd_reference: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "TvdReference",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        },
    )
    local_depth3d_crs: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "LocalDepth3dCrs",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        },
    )


@dataclass
class UnstructuredColumnEdges:
    """Column edges are used to construct the index for faces.

    For unstructured column-layer grids, the column edge indices must be
    defined explicitly. Column edges are not required to describe lowest
    order grid geometry, but may be needed for higher order geometries
    or properties.

    :ivar count: Number of unstructured column edges in this grid. Must
        be positive.
    :ivar pillars_per_column_edge: Definition of the column edges in
        terms of the pillars-per-column edge. Pillar count per edge is
        usually 2, but the list-of-lists construction is used to allow
        column edges to be defined by more than 2 pillars.
    """

    count: Optional[int] = field(
        default=None,
        metadata={
            "name": "Count",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
            "min_inclusive": 1,
        },
    )
    pillars_per_column_edge: Optional[JaggedArray] = field(
        default=None,
        metadata={
            "name": "PillarsPerColumnEdge",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        },
    )


@dataclass
class UnstructuredGridHingeNodeFaces:
    """Hinge nodes define a triangulated interpolation on a cell face.

    In practice, they arise on the K faces of column layer cells and are used to add additional geometric resolution to the shape of the cell. The specification of triangulated interpolation also uniquely defines the interpolation schema on the cell face, and hence the cell volume.
    For an unstructured cell grid, the hinge node faces need to be defined explicitly.
    This hinge node faces data-object is optional and is only expected to be used if the hinge node faces higher order grid point attachment arises. Hinge node faces are not supported for property attachment. Instead use a subrepresentation or an attachment kind of faces or faces per cell.
    BUSINESS RULE: Each cell must have either 0 or 2 hinge node faces, so that the two hinge nodes for the cell may be used to define a cell center line and a cell thickness.

    :ivar count: Number of K faces. This count must be positive.
    :ivar face_indices: List of faces to be identified as K faces for
        hinge node geometry attachment. BUSINESS RULE: Array length
        equals K face count.
    """

    count: Optional[int] = field(
        default=None,
        metadata={
            "name": "Count",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
            "min_inclusive": 1,
        },
    )
    face_indices: Optional[AbstractIntegerArray] = field(
        default=None,
        metadata={
            "name": "FaceIndices",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        },
    )


@dataclass
class ViewerKindExt:
    """
    Allows you to use custom viewer kinds in addition to the ViewerKind
    enumeration.
    """

    value: Union[ViewerKind, str] = field(
        default="",
        metadata={
            "pattern": r".*:.*",
        },
    )


@dataclass
class VolumeShell:
    """The shell or envelope of a geologic unit.

    It is a collection of macro faces. Each macro face is defined by a
    triplet of values, each value being at the same index in the three
    arrays contained in this class.

    :ivar patch_indices_of_representation: Each index identifies the
        surface representation patch describing the macro face.
    :ivar representation_indices: Each index identifies the macro face
        surface representation by its index in the list of
        representations contained in the organization.
    :ivar side_is_plus: Each index identifies the side of the macro
        face.
    """

    patch_indices_of_representation: Optional[IntegerExternalArray] = field(
        default=None,
        metadata={
            "name": "PatchIndicesOfRepresentation",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        },
    )
    representation_indices: Optional[IntegerExternalArray] = field(
        default=None,
        metadata={
            "name": "RepresentationIndices ",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        },
    )
    side_is_plus: Optional[BooleanExternalArray] = field(
        default=None,
        metadata={
            "name": "SideIsPlus",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        },
    )


@dataclass
class WellboreTrajectoryParentIntersection:
    """
    For a wellbore trajectory in a multi-lateral well, indicates the MD of the
    kickoff point where the trajectory begins and the corresponding MD of the
    parent trajectory.

    :ivar kickoff_md: KickoffMd is the measured depth for the start of
        the child trajectory, as defined within the child.
    :ivar parent_md: If the kickoff MD in the child (KickoffMd) is
        different from the kickoff MD in the parent (ParentMd), then
        specify the ParentMD here. If not specified, then these two MD's
        are implied to be identical.
    :ivar parent_trajectory:
    """

    kickoff_md: Optional[float] = field(
        default=None,
        metadata={
            "name": "KickoffMd",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        },
    )
    parent_md: Optional[float] = field(
        default=None,
        metadata={
            "name": "ParentMd",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        },
    )
    parent_trajectory: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "ParentTrajectory",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        },
    )


@dataclass
class WitsmlWellWellbore:
    """
    Reference to the WITSML wellbore that this wellbore feature is based on.
    """

    witsml_well: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "WitsmlWell",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        },
    )
    witsml_wellbore: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "WitsmlWellbore",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        },
    )


@dataclass
class AbstractOrganizationInterpretation(AbstractFeatureInterpretation):
    """The main class used to group features into meaningful units as a step in
    working towards the goal of building an earth model (the organization of all
    other organizations in RESQML).

    An organization interpretation:
    - Is typically comprised of one stack of its contained elements.
    - May be built on other organization interpretations.
    Typically contains:
    - contacts between the elements of this stack among themselves.
    - contacts between the stack elements and other organization elements.
    """

    contact_interpretation: List[AbstractContactInterpretationPart] = field(
        default_factory=list,
        metadata={
            "name": "ContactInterpretation",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        },
    )


@dataclass
class AbstractParametricLineGeometry(AbstractGeometry):
    """
    The abstract class for defining a single parametric line.
    """


@dataclass
class AbstractPlaneGeometry(AbstractGeometry):
    """
    The abstract class for all geometric values defined by planes.
    """


@dataclass
class AbstractSurfaceRepresentation(AbstractRepresentation):
    """Parent class of structural surface representations, which can be bounded by
    an outer ring and has inner rings.

    These surfaces may consist of one or more patches.
    """

    surface_role: Optional[SurfaceRole] = field(
        default=None,
        metadata={
            "name": "SurfaceRole",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        },
    )
    boundaries: List[PatchBoundaries] = field(
        default_factory=list,
        metadata={
            "name": "Boundaries",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        },
    )


@dataclass
class AbstractTechnicalFeature(AbstractFeature):
    """Objects that exist by the action of humans.

    Examples include: wells and all they may contain, seismic surveys (surface, permanent water bottom), or injected fluid volumes. Because the decision to deploy such equipment is the result of studies or decisions by humans, technical features are usually not subject to the same kind of large changes in interpretation as geologic features. However, they are still subject to measurement error and other sources of uncertainty, and so still can be considered as subject to "interpretation".
    """


@dataclass
class AbstractValuesProperty(AbstractProperty):
    """Base class for property values.

    Each derived element provides specific property values, including
    point property in support of geometries.

    :ivar values_for_patch: If the rep has no explicit patch, use only 1
        ValuesForPatch.  If the rep has &gt; 1 explicit patch, use as
        many ValuesforPatch as patches of the rep. The ordering of
        ValuesForPatch matches the ordering of the patches in the xml
        document of the representation.
    :ivar facet:
    """

    values_for_patch: List[AbstractValueArray] = field(
        default_factory=list,
        metadata={
            "name": "ValuesForPatch",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "min_occurs": 1,
        },
    )
    facet: List[PropertyKindFacet] = field(
        default_factory=list,
        metadata={
            "name": "Facet",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        },
    )


@dataclass
class BinaryContactInterpretationPart(AbstractContactInterpretationPart):
    """The main class for data describing an opinion of the contact between two
    geologic feature-interpretations.

    - A contact interpretation between two surface geological boundaries is usually a line.
    - A contact interpretation between two volumes (rock feature-interpretation) is usually a surface.
    This class allows you to build a formal sentence—in the pattern of subject-verb-direct object—which is used to describe the construction of a node, line, or surface contact. It is also possible to attach a primary and a secondary qualifier to the subject and to the direct object.
    For more information, see the RESQML Technical Usage Guide.
    For example, one contact interpretation can be described by a sentence such as:
    The interpreted fault named F1 interp on its hanging wall side splits the interpreted horizon named H1 Interp on both its sides.
    Subject = F1 Interp, with qualifier "hanging wall side"
    Verb = splits
    Direct Object = H1 Interp, with qualifier "on both sides"

    :ivar direct_object: Data-object reference (by UUID link) to a
        geologic feature-interpretation, which is the direct object of
        the sentence that defines how the contact was constructed.
    :ivar subject: Data-object reference (by UUID link) to a geologic
        feature-interpretation, which is the subject of the sentence
        that defines how the contact was constructed.
    :ivar verb:
    """

    direct_object: Optional[ContactElement] = field(
        default=None,
        metadata={
            "name": "DirectObject",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        },
    )
    subject: Optional[ContactElement] = field(
        default=None,
        metadata={
            "name": "Subject",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        },
    )
    verb: Optional[ContactVerb] = field(
        default=None,
        metadata={
            "name": "Verb",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        },
    )


@dataclass
class BoundaryFeature(AbstractFeature):
    """An interface between two objects, such as horizons and faults.

    It is a surface object.
    A RockVolumeFeature is a geological feature (which is the general concept that refers to the various categories of geological objects that exist in the natural world).
    For example: the stratigraphic boundaries, the =geobody boundaries or the fluid boundaries that are present before production. To simplify the hierarchy of concepts, the geological feature is not represented in the RESQML design.
    """

    class Meta:
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class BoundaryFeatureInterpretation(AbstractFeatureInterpretation):
    """The main class for data describing an opinion of a surface feature between
    two volumes.

    BUSINESS RULE: The data-object reference (of type "interprets") must reference only a boundary feature.

    :ivar older_possible_age: A value in years of the age offset between
        the DateTime attribute value and the DateTime of a
        GeologicalEvent occurrence of generation. When it represents a
        geological event that happened in the past, this value must be
        POSITIVE.
    :ivar younger_possible_age: A value in years of the age offset
        between the DateTime attribute value and the DateTime of a
        GeologicalEvent occurrence of generation. When it represents a
        geological event that happened in the past, this value must be
        POSITIVE.
    :ivar absolute_age:
    """

    class Meta:
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"

    older_possible_age: Optional[int] = field(
        default=None,
        metadata={
            "name": "OlderPossibleAge",
            "type": "Element",
        },
    )
    younger_possible_age: Optional[int] = field(
        default=None,
        metadata={
            "name": "YoungerPossibleAge",
            "type": "Element",
        },
    )
    absolute_age: Optional[GeologicTime] = field(
        default=None,
        metadata={
            "name": "AbsoluteAge",
            "type": "Element",
        },
    )


@dataclass
class CellOverlap:
    """Optional cell volume overlap information between the current grid (the
    child) and the parent grid.

    Use this data-object when the child grid has an explicitly defined
    geometry, and these relationships cannot be inferred from the regrid
    descriptions.

    :ivar count: Number of parent-child cell overlaps. Must be positive.
    :ivar parent_child_cell_pairs: (Parent cell index, child cell index)
        pair for each overlap. BUSINESS RULE: Length of array must equal
        2 x overlapCount.
    :ivar overlap_volume:
    """

    count: Optional[int] = field(
        default=None,
        metadata={
            "name": "Count",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
            "min_inclusive": 1,
        },
    )
    parent_child_cell_pairs: Optional[AbstractIntegerArray] = field(
        default=None,
        metadata={
            "name": "ParentChildCellPairs",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        },
    )
    overlap_volume: Optional[OverlapVolume] = field(
        default=None,
        metadata={
            "name": "OverlapVolume",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        },
    )


@dataclass
class ColorMapDictionary(AbstractObject):
    """
    A container for color maps.
    """

    class Meta:
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"

    color_map: List[AbstractColorMap] = field(
        default_factory=list,
        metadata={
            "name": "ColorMap",
            "type": "Element",
        },
    )


@dataclass
class ColumnSubnodePatch(SubnodePatch):
    """
    Use this subnode construction if the number of subnodes per object varies from
    column to column, but does not vary from layer to layer.

    :ivar subnode_count_per_object: Number of subnodes per object, with
        a different number in each column of the grid.
    """

    subnode_count_per_object: Optional[AbstractIntegerArray] = field(
        default=None,
        metadata={
            "name": "SubnodeCountPerObject",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        },
    )


@dataclass
class ContinuousColorMap(AbstractColorMap):
    """
    A color map associating a double value to a color.

    :ivar interpolation_domain: The domain for the interpolation between
        color map entries.
    :ivar interpolation_method: The method for the interpolation between
        color map entries.
    :ivar entry:
    """

    class Meta:
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"

    interpolation_domain: Optional[InterpolationDomain] = field(
        default=None,
        metadata={
            "name": "InterpolationDomain",
            "type": "Element",
            "required": True,
        },
    )
    interpolation_method: Optional[InterpolationMethod] = field(
        default=None,
        metadata={
            "name": "InterpolationMethod",
            "type": "Element",
            "required": True,
        },
    )
    entry: List[ContinuousColorMapEntry] = field(
        default_factory=list,
        metadata={
            "name": "Entry",
            "type": "Element",
            "min_occurs": 2,
        },
    )


@dataclass
class DefaultGraphicalInformation(AbstractGraphicalInformation):
    """
    Either for Feature, Interp or representation, marker.

    :ivar viewer_id: Use this especially to differentiate between two
        viewers of the same kind
    :ivar viewer_kind: The kind of viewer where this graphical
        information is supposed to be used.
    :ivar indexable_element_info:
    """

    viewer_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ViewerId",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        },
    )
    viewer_kind: Optional[Union[ViewerKind, str]] = field(
        default=None,
        metadata={
            "name": "ViewerKind",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
            "pattern": r".*:.*",
        },
    )
    indexable_element_info: List[
        AbstractGraphicalInformationForIndexableElement
    ] = field(
        default_factory=list,
        metadata={
            "name": "IndexableElementInfo",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "min_occurs": 1,
        },
    )


@dataclass
class DiscreteColorMap(AbstractColorMap):
    """A color map associating an integer value to a color.

    BUSINESS RULE: When using a discrete color map for a continuous property the property value will be equal to the next lowest integer in the color map.  For example a color map of 10, 20, 30, etc., and a continuous property value of 16.5 will result in a value of 10 for the minimum.
    """

    class Meta:
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"

    entry: List[DiscreteColorMapEntry] = field(
        default_factory=list,
        metadata={
            "name": "Entry",
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass
class EarthModelInterpretation(AbstractFeatureInterpretation):
    """An earth model interpretation has the specific role of gathering at most:
    - one StratigraphicOrganizationInterpretation
    - One or several StructuralOrganizationInterpretations
    - One or several RockFluidOrganizationInterpretations
    BUSINESS RULE: An earth model Interpretation interprets only a model feature."""

    class Meta:
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"

    stratigraphic_occurrences: List[DataObjectReference] = field(
        default_factory=list,
        metadata={
            "name": "StratigraphicOccurrences",
            "type": "Element",
        },
    )
    wellbore_interpretation_set: List[DataObjectReference] = field(
        default_factory=list,
        metadata={
            "name": "WellboreInterpretationSet",
            "type": "Element",
        },
    )
    stratigraphic_column: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "StratigraphicColumn",
            "type": "Element",
        },
    )
    structure: List[DataObjectReference] = field(
        default_factory=list,
        metadata={
            "name": "Structure",
            "type": "Element",
        },
    )
    fluid: List[DataObjectReference] = field(
        default_factory=list,
        metadata={
            "name": "Fluid",
            "type": "Element",
        },
    )


@dataclass
class FluidIntervalBoundary(MarkerBoundary):
    """
    This represents a boundary between two intervals where at least one side of the
    boundary is a fluid.
    """


@dataclass
class GenericFeatureInterpretation(AbstractFeatureInterpretation):
    """An interpretation of a feature that is not specialized.

    For example, use it when the specialized type of the associated
    feature is not known. For example, to set up a
    StructuralOrganizationInterpretation you must reference the
    interpretations of each feature you want to include. These features
    must include FrontierFeatures which have no interpretations because
    they are technical features. For consistency of design of the
    StructuralOrganizationInterpretation, create a
    GenericFeatureInterpretation for each FrontierFeature.
    """

    class Meta:
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class GeologicUnitInterpretation(AbstractFeatureInterpretation):
    """The main class for data describing an opinion of an originally continuous
    rock volume individualized in view of some characteristic property (e.g.,
    physical, chemical, temporal) defined by GeologicUnitComposition and/or
    GeologicUnitMaterialImplacement, which can have a 3D defined shape.

    BUSINESS RULE: The data object reference (of type "interprets") must reference only a rock volume feature.
    In an earth model, a geological unit interrupted by faults may consist of several disconnected rock volumes.

    :ivar geologic_unit_composition:
    :ivar geologic_unit_material_emplacement: Attribute specifying
        whether the GeologicalUnitIntepretation is intrusive or not.
    :ivar geologic_unit3d_shape: 3D shape of the geologic unit.
    :ivar depositional_environment:
    :ivar depositional_facies:
    """

    class Meta:
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"

    geologic_unit_composition: Optional[Union[LithologyKind, str]] = field(
        default=None,
        metadata={
            "name": "GeologicUnitComposition",
            "type": "Element",
            "pattern": r".*:.*",
        },
    )
    geologic_unit_material_emplacement: Optional[
        GeologicUnitMaterialEmplacement
    ] = field(
        default=None,
        metadata={
            "name": "GeologicUnitMaterialEmplacement",
            "type": "Element",
        },
    )
    geologic_unit3d_shape: Optional[Union[Shape3D, str]] = field(
        default=None,
        metadata={
            "name": "GeologicUnit3dShape",
            "type": "Element",
            "pattern": r".*:.*",
        },
    )
    depositional_environment: Optional[
        Union[DepositionalEnvironmentKind, str]
    ] = field(
        default=None,
        metadata={
            "name": "DepositionalEnvironment",
            "type": "Element",
            "pattern": r".*:.*",
        },
    )
    depositional_facies: Optional[Union[DepositionalFaciesKind, str]] = field(
        default=None,
        metadata={
            "name": "DepositionalFacies",
            "type": "Element",
            "pattern": r".*:.*",
        },
    )


@dataclass
class GraphicalInformationForEdges(
    AbstractGraphicalInformationForIndexableElement
):
    """
    Graphical information for edges.

    :ivar display_space:
    :ivar pattern: The pattern of the edge.
    :ivar thickness: The thickness of the edge.
    :ivar use_interpolation_between_nodes: Use color and size
        interpolation between nodes.
    """

    display_space: Optional[DisplaySpace] = field(
        default=None,
        metadata={
            "name": "DisplaySpace",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        },
    )
    pattern: Optional[Union[EdgePattern, str]] = field(
        default=None,
        metadata={
            "name": "Pattern",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "pattern": r".*:.*",
        },
    )
    thickness: Optional[LengthMeasureExt] = field(
        default=None,
        metadata={
            "name": "Thickness",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        },
    )
    use_interpolation_between_nodes: Optional[bool] = field(
        default=None,
        metadata={
            "name": "UseInterpolationBetweenNodes",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        },
    )


@dataclass
class GraphicalInformationForFaces(
    AbstractGraphicalInformationForIndexableElement
):
    """
    Graphical information for faces.

    :ivar applies_on_right_handed_face: If true the graphical
        information only applies to the right handed side of the face.
        If false, it only applies to the left handed side of the face.
        If not present the graphical information applies to both sides
        of faces.
    :ivar use_interpolation_between_nodes: Interpolate the values all
        along the face based on fixed value set on nodes.
    """

    applies_on_right_handed_face: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AppliesOnRightHandedFace",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        },
    )
    use_interpolation_between_nodes: Optional[bool] = field(
        default=None,
        metadata={
            "name": "UseInterpolationBetweenNodes",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        },
    )


@dataclass
class GraphicalInformationForNodes(
    AbstractGraphicalInformationForIndexableElement
):
    """
    Graphical information for nodes.

    :ivar constant_size: A size for all the nodes. Not defined if
        ActiveSizeInformationIndex is defined.
    :ivar display_space:
    :ivar show_symbol_every: Allows you to show only a subset of nodes
        (instead of all of them).
    :ivar symbol: The symbol used to visualize a single node.
    """

    constant_size: Optional[LengthMeasureExt] = field(
        default=None,
        metadata={
            "name": "ConstantSize",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        },
    )
    display_space: Optional[DisplaySpace] = field(
        default=None,
        metadata={
            "name": "DisplaySpace",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        },
    )
    show_symbol_every: Optional[int] = field(
        default=None,
        metadata={
            "name": "ShowSymbolEvery",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        },
    )
    symbol: Optional[Union[NodeSymbol, str]] = field(
        default=None,
        metadata={
            "name": "Symbol",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "pattern": r".*:.*",
        },
    )


@dataclass
class GraphicalInformationForVolumes(
    AbstractGraphicalInformationForIndexableElement
):
    """
    Graphical information for volumes.

    :ivar use_interpolation_between_nodes: Interpolate the values all
        along the volume based on a fixed value set on nodes.
    """

    use_interpolation_between_nodes: Optional[bool] = field(
        default=None,
        metadata={
            "name": "UseInterpolationBetweenNodes",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        },
    )


@dataclass
class GraphicalInformationForWholeObject(
    AbstractGraphicalInformationForIndexableElement
):
    """
    Graphical information for the whole data object.

    :ivar active_contour_line_set_information_index: Display the contour
        line of the visualized data object according to information at a
        particular index of the GraphicalInformationSet.
    :ivar display_title: Display the title of the visualized data object
        next to it.
    """

    active_contour_line_set_information_index: Optional[int] = field(
        default=None,
        metadata={
            "name": "ActiveContourLineSetInformationIndex",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        },
    )
    display_title: Optional[bool] = field(
        default=None,
        metadata={
            "name": "DisplayTitle",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        },
    )


@dataclass
class GridConnectionSetRepresentation(AbstractRepresentation):
    """Representation that consists of a list of connections between grid cells,
    potentially on different grids.

    Connections are in the form of (Grid,Cell,Face)1&lt;=&gt;(Grid,Cell,Face)2 and are stored as three integer pair arrays corresponding to these six elements.
    Grid connection sets are the preferred means of representing faults on a grid. The use of cell-face-pairs is more complete than single cell-faces, which are missing a corresponding cell face entry, and only provide an incomplete representation of the topology of a fault.
    Unlike what is sometimes the case in reservoir simulation software, RESQML does not distinguish between standard and non-standard connections.
    Within RESQML, if a grid connection corresponds to a "nearest neighbor" as defined by the cell indices, then it is never additive to the implicit nearest neighbor connection.
    BUSINESS RULE: A single cell-face-pair should not appear within more than a single grid connection set. This rule is designed to simplify the interpretation of properties assigned to multiple grid connection sets, which might otherwise have the same property defined more than once on a single connection, with no clear means of resolving the multiple values.

    :ivar count: count of connections. Must be positive.
    :ivar cell_index_pairs: 2 x #Connections array of cell indices for
        (Cell1,Cell2) for each connection.
    :ivar grid_index_pairs: 2 x #Connections array of grid indices for
        (Cell1,Cell2) for each connection. The grid indices are obtained
        from the grid index pairs. If only a single grid is referenced
        from the grid index, then this array need not be used. BUSINESS
        RULE: If more than one grid index pair is referenced, then this
        array should appear.
    :ivar local_face_per_cell_index_pairs: Optional 2 x #Connections
        array of local face-per-cell indices for (Cell1,Cell2) for each
        connection. Local face-per-cell indices are used because global
        face indices need not have been defined. If no face-per-cell
        definition occurs as part of the grid representation, e.g., for
        a block-centered grid, then this array need not appear.
    :ivar connection_interpretations:
    :ivar grid:
    """

    class Meta:
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"

    count: Optional[int] = field(
        default=None,
        metadata={
            "name": "Count",
            "type": "Element",
            "required": True,
            "min_inclusive": 1,
        },
    )
    cell_index_pairs: Optional[AbstractIntegerArray] = field(
        default=None,
        metadata={
            "name": "CellIndexPairs",
            "type": "Element",
            "required": True,
        },
    )
    grid_index_pairs: Optional[AbstractIntegerArray] = field(
        default=None,
        metadata={
            "name": "GridIndexPairs",
            "type": "Element",
        },
    )
    local_face_per_cell_index_pairs: Optional[AbstractIntegerArray] = field(
        default=None,
        metadata={
            "name": "LocalFacePerCellIndexPairs",
            "type": "Element",
        },
    )
    connection_interpretations: Optional[ConnectionInterpretations] = field(
        default=None,
        metadata={
            "name": "ConnectionInterpretations",
            "type": "Element",
        },
    )
    grid: List[DataObjectReference] = field(
        default_factory=list,
        metadata={
            "name": "Grid",
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass
class LocalGridSet(AbstractObject):
    """Used to activate and/or deactivate the specified children grids as local
    grids on their parents.

    Once activated, this object indicates that a child grid replaces
    local portions of the corresponding parent grid. Specifically,
    properties and/or geometry in the region of a parent window will be
    stored on both the parent and child grids, usually with differing
    spatial resolutions. The choice of whether non-null properties are
    stored on both grids, or only the child grid, is application
    specific. Parentage is inferred from the child grid construction.
    Without a grid set activation, the local grids are always active.
    Otherwise, the grid set activation is used to activate and/or
    deactivate the local grids in the set at specific times.
    """

    class Meta:
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"

    activation: Optional[Activation] = field(
        default=None,
        metadata={
            "name": "Activation",
            "type": "Element",
        },
    )
    child_grid: List[DataObjectReference] = field(
        default_factory=list,
        metadata={
            "name": "ChildGrid",
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass
class Model(AbstractFeature):
    """The explicit description of the relationships between geologic features,
    such as rock features (e.g. stratigraphic units, geobodies, phase unit) and
    boundary features (e.g., genetic, tectonic, and fluid boundaries).

    In general, this concept is usually called an "earth model", but it
    is not called that in RESQML. In RESQML, model is not to be confused
    with the concept of earth model organization interpretation.
    """

    class Meta:
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class MultipleContactInterpretationPart(AbstractContactInterpretationPart):
    """Describes multiple interface contacts of geologic feature-interpretations
    (compared to a binary contact).

    A composition of several contact interpretations.

    :ivar with_value: Indicates a list of binary contacts (by their
        UUIDs) that participate in this multiple-part contact.
    """

    with_value: List[int] = field(
        default_factory=list,
        metadata={
            "name": "With",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "min_occurs": 1,
            "min_inclusive": 0,
        },
    )


@dataclass
class NonSealedContact(AbstractSurfaceFrameworkContact):
    """
    Defines a non-sealed contact representation, meaning that this contact
    representation is defined by a geometry.
    """

    patches: List[ContactPatch] = field(
        default_factory=list,
        metadata={
            "name": "Patches",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        },
    )
    geometry: Optional[AbstractGeometry] = field(
        default=None,
        metadata={
            "name": "Geometry",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        },
    )


@dataclass
class ParametricLineArray(AbstractParametricLineArray):
    """Defines an array of parametric lines of multiple kinds.

    For more information, see the RESQML Technical Usage Guide.
    In general, a parametric line is unbounded so the interpolant in the first or last interval is used as an extrapolating function.
    Special Cases:
    (1) Natural cubic splines with only two control points reduce to linear interpolation.
    (2) If required but not defined, tangent vectors at a spline knot are calculated from the control point data using a quadratic fit to the control point and the two adjacent control points (if internal) or, if at an edge, by a vanishing second derivative. This calculation reduces locally to a natural spline.
    (3) If not expected but provided, then extraneous information is to be ignored, e.g., tangent vectors for linear splines.
    Vertical:
    (1) Control points are (X,Y,-).
    (2) Parameter values are interpreted as depth =&gt; (X,Y,Z), where the depth to Z conversion depends on the vertical CRS direction.
    Piecewise Linear:
    (1) Control points are (P,X,Y,Z).
    (2) Piecewise interpolation in (X,Y,Z) as a linear function of P.
    Natural Cubic:
    (1) Control points are (P,X,Y,Z).
    (2) First and second derivatives at each knot are inferred from a quadratic fit to the two adjacent control points, if internal, or, if external knots, by specifying a vanishing second derivative.
    Tangential Cubic and Minimum-Curvature.
    (1) Control points are (P,X,Y,Z).
    (2) Tangent vectors are (P,TX,TY,TZ). Tangent vectors are defined as the derivative of position with respect to the parameter. If the parameter is arc-length, then the tangent vectors are unit vectors, but not otherwise.
    (3) Interpolating minimum-curvature basis functions obtained by a circular arc construction. This differs from the "drilling" algorithm in which the parameter must be arc length.
    Z Linear Cubic:
    (1) (X,Y) follow a natural cubic spline and Z follows a linear spline.
    (2) On export, to go from Z to P, the RESQML "software writer" first needs to determine the interval and then uses linearity in Z to determine P.
    (3) On import, a RESQML "software reader" converts from P to Z using piecewise linear interpolation, and from P to X and Y using natural cubic spline interpolation. Other than the differing treatment of Z from X and Y, these are completely generic interpolation algorithms.
    (4) The use of P instead of Z for interpolation allows support for over-turned reservoir structures and removes any apparent discontinuities in parametric derivatives at the spline knots.

    :ivar control_point_parameters: An array of explicit control point
        parameters for all of the control points on each of the
        parametric lines. If you cannot provide enough control point
        parameters for a parametric line, then pad with NaN values.
        BUSINESS RULE: The parametric values must be strictly
        monotonically increasing on each parametric line.
    :ivar control_points: An array of 3D points for all of the control
        points on each of the parametric lines. The number of control
        points per line is given by the KnotCount. Control points are
        ordered by lines going fastest, then by knots going slowest. If
        you cannot provide enough control points for a parametric line,
        then pad with NaN values.
    :ivar knot_count: The first dimension of the control point, control
        point parameter, and tangent vector arrays for the parametric
        splines. The Knot Count is typically chosen to be the maximum
        number of control points, parameters or tangent vectors on any
        parametric line in the array of parametric lines.
    :ivar line_kind_indices: An array of integers indicating the
        parametric line kind. 0 = vertical 1 = linear spline 2 = natural
        cubic spline 3 = tangential cubic spline 4 = Z linear cubic
        spline 5 = minimum-curvature spline null value: no line Size =
        #Lines, e.g., (1D or 2D)
    :ivar tangent_vectors: An optional array of tangent vectors for all
        of the control points on each of the tangential cubic and
        minimum-curvature parametric lines. Used only if tangent vectors
        are present. The number of tangent vectors per line is given by
        the KnotCount for these spline types. Described as a 1D array,
        the tangent vector array is divided into segments of length Knot
        Count, with null (NaN) values added to each segment to fill it
        up. Size = Knot Count x #Lines, e.g., 2D or 3D BUSINESS RULE:
        For all lines other than the cubic and minimum-curvature
        parametric lines, this array should not appear. For these line
        kinds, there should be one tangent vector for each control
        point. If a tangent vector is missing, then it is computed in
        the same fashion as for a natural cubic spline. Specifically, to
        obtain the tangent at internal knots, the control points are fit
        by a quadratic function with the two adjacent control points. At
        edge knots, the second derivative vanishes.
    :ivar parametric_line_intersections:
    """

    control_point_parameters: Optional[AbstractFloatingPointArray] = field(
        default=None,
        metadata={
            "name": "ControlPointParameters",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        },
    )
    control_points: Optional[AbstractPoint3DArray] = field(
        default=None,
        metadata={
            "name": "ControlPoints",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        },
    )
    knot_count: Optional[int] = field(
        default=None,
        metadata={
            "name": "KnotCount",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
            "min_inclusive": 1,
        },
    )
    line_kind_indices: Optional[AbstractIntegerArray] = field(
        default=None,
        metadata={
            "name": "LineKindIndices",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        },
    )
    tangent_vectors: Optional[AbstractPoint3DArray] = field(
        default=None,
        metadata={
            "name": "TangentVectors",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        },
    )
    parametric_line_intersections: Optional[
        ParametricLineIntersections
    ] = field(
        default=None,
        metadata={
            "name": "ParametricLineIntersections",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        },
    )


@dataclass
class Point3DLatticeArray(AbstractPoint3DArray):
    """Describes a lattice array of points obtained by sampling from along a multi-
    dimensional lattice.

    Each dimension of the lattice can be uniformly or irregularly
    spaced.

    :ivar all_dimensions_are_orthogonal: The optional element that
        indicates that the offset vectors for each direction are
        mutually orthogonal to each other. This meta-information is
        useful to remove any doubt of orthogonality in case of numerical
        precision issues. BUSINESS RULE: If you don't know it or if only
        one lattice dimension is given, do not provide this element.
    :ivar origin: The origin location of the lattice given as XYZ
        coordinates.
    :ivar dimension:
    """

    class Meta:
        name = "Point3dLatticeArray"

    all_dimensions_are_orthogonal: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AllDimensionsAreOrthogonal",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        },
    )
    origin: Optional[Point3D] = field(
        default=None,
        metadata={
            "name": "Origin",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        },
    )
    dimension: List[Point3DLatticeDimension] = field(
        default_factory=list,
        metadata={
            "name": "Dimension",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "min_occurs": 1,
        },
    )


@dataclass
class PointGeometry(AbstractGeometry):
    """
    The geometry of a set of points defined by their location in the local CRS,
    with optional seismic coordinates.
    """

    points: Optional[AbstractPoint3DArray] = field(
        default=None,
        metadata={
            "name": "Points",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        },
    )
    seismic_coordinates: Optional[AbstractSeismicCoordinates] = field(
        default=None,
        metadata={
            "name": "SeismicCoordinates",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        },
    )


@dataclass
class PointsProperty(AbstractProperty):
    """
    Represents the geometric information that should *not* be used as
    representation geometry, but should be used in another context where the
    location or geometrical vectorial distances are needed.

    :ivar points_for_patch: Geometric points (or vectors) to be attached
        to the specified indexable elements.
    """

    class Meta:
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"

    points_for_patch: List[AbstractPoint3DArray] = field(
        default_factory=list,
        metadata={
            "name": "PointsForPatch",
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass
class Regrid:
    """One-dimensional I, J, or K refinement and coarsening regrid specification.

    The regrid description is organized using intervals. Within each
    interval, the number of parent and child cells is specified. Parent
    and child grid cell faces are aligned at interval boundaries. By
    default, child cells are uniformly sized within an interval unless
    weights are used to modify their size. If the child grid is a root
    grid with an independent geometry, then there will usually be only a
    single interval for a regrid, because internal cell faces are not
    necessarily aligned.

    :ivar initial_index_on_parent_grid: 0-based index for the placement
        of the window on the parent grid.
    :ivar intervals:
    """

    initial_index_on_parent_grid: Optional[int] = field(
        default=None,
        metadata={
            "name": "InitialIndexOnParentGrid",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
            "min_inclusive": 0,
        },
    )
    intervals: Optional[Intervals] = field(
        default=None,
        metadata={
            "name": "Intervals",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        },
    )


@dataclass
class RepresentationSetRepresentation(AbstractRepresentation):
    """The parent class of the framework representations.

    It is used to group together individual representations to represent
    a "bag" of representations. If the individual representations are
    all of the same, then you can indicate that the set is homogenous.
    These "bags" do not imply any geologic consistency. For example, you
    can define a set of wellbore frames, a set of wellbore trajectories,
    a set of blocked wellbores. Because the framework representations
    inherit from this class, they inherit the capability to gather
    individual representations into sealed and non-sealed surface
    framework representations, or sealed volume framework
    representations. For more information, see the RESQML Technical
    Usage Guide.

    :ivar is_homogeneous: Indicates that all of the selected
        representations are of a single kind.
    :ivar representation:
    """

    class Meta:
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"

    is_homogeneous: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsHomogeneous",
            "type": "Element",
            "required": True,
        },
    )
    representation: List[DataObjectReference] = field(
        default_factory=list,
        metadata={
            "name": "Representation",
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass
class RockVolumeFeature(AbstractFeature):
    """A continuous portion of rock material bounded by definite rock boundaries.

    It is a volume object. Some of these rock volumes are "static",
    while others are "dynamic". Reservoir fluids are dynamic because
    their properties, geometries, and quantities may change over time
    during the course of field production. A RockVolume feature is a
    geological feature--which is the general concept that refers to the
    various categories of geological objects that exist in the natural
    world, for example, the rock volume or the fluids that are present
    before production. The geological feature is not represented in the
    RESQML design.
    """

    class Meta:
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class SealedContact(AbstractSurfaceFrameworkContact):
    """Sealed contact elements that indicate that 2 or more contact patches are
    partially or totally colocated or equivalent.

    For possible types of identity, see IdentityKind.

    :ivar identical_node_indices: Indicates which nodes (identified by
        their common index in all contact patches) of the contact
        patches are identical. If this list is not present, then it
        indicates that all nodes in each representation are identical,
        on an element-by-element level.
    :ivar identity_kind: Must be one of the enumerations in
        IdentityKind.
    :ivar patches:
    """

    identical_node_indices: Optional[AbstractIntegerArray] = field(
        default=None,
        metadata={
            "name": "IdenticalNodeIndices",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        },
    )
    identity_kind: Optional[IdentityKind] = field(
        default=None,
        metadata={
            "name": "IdentityKind",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        },
    )
    patches: List[ContactPatch] = field(
        default_factory=list,
        metadata={
            "name": "Patches",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "min_occurs": 2,
        },
    )


@dataclass
class Seismic2DCoordinates(AbstractSeismicCoordinates):
    """A group of 2D seismic coordinates that stores the 1-to-1 mapping between
    geometry patch coordinates (usually X, Y, Z) and trace or inter-trace positions
    on a seismic line.

    BUSINESS RULE: This patch must reference a geometry patch by its UUID.

    :ivar line_abscissa: The sequence of trace or inter-trace positions
        that correspond to the geometry coordinates. BUSINESS RULE: Both
        sequences must be in the same order.
    :ivar vertical_coordinates: The sequence of vertical sample or
        inter-sample positions that corresponds to the geometry
        coordinates. BUSINESS RULE: Sequence must be in the same order
        as the previous one.
    """

    class Meta:
        name = "Seismic2dCoordinates"

    line_abscissa: Optional[AbstractFloatingPointArray] = field(
        default=None,
        metadata={
            "name": "LineAbscissa",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        },
    )
    vertical_coordinates: Optional[AbstractFloatingPointArray] = field(
        default=None,
        metadata={
            "name": "VerticalCoordinates",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        },
    )


@dataclass
class Seismic2DPostStackRepresentation(AbstractRepresentation):
    """The feature of this representation should be the same survey feature as the
    associated PolylineRepresentation represents..

    The indexing convention (mainly for associated properties) is :
    - Trace sample goes fastest
    - Then polyline node slowest
    The indexing convention only applies to HDF datasets (not SEGY file).
    A whole SEGY file can be referenced in properties of this representation, but not partial files.

    :ivar seismic_line_sub_sampling: This array must be one dimension
        and count must be the node count in the associated seismic line
        i.e., polylineRepresentation. The index is based on array
        indexing, not on index labeling of traces. The values of the
        integer lattice array are the increments between 2 consecutive
        subsampled nodes.
    :ivar trace_sampling: Defines the sampling in the vertical dimension
        of the representation. This array must be one dimension. The
        values are given with respect to the associated local CRS.
    :ivar seismic_line_representation:
    :ivar local_crs:
    """

    class Meta:
        name = "Seismic2dPostStackRepresentation"
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"

    seismic_line_sub_sampling: Optional[IntegerLatticeArray] = field(
        default=None,
        metadata={
            "name": "SeismicLineSubSampling",
            "type": "Element",
            "required": True,
        },
    )
    trace_sampling: Optional[FloatingPointLatticeArray] = field(
        default=None,
        metadata={
            "name": "TraceSampling",
            "type": "Element",
            "required": True,
        },
    )
    seismic_line_representation: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "SeismicLineRepresentation",
            "type": "Element",
            "required": True,
        },
    )
    local_crs: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "LocalCrs",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Seismic3DCoordinates(AbstractSeismicCoordinates):
    """
    The 1-to-1 mapping between geometry coordinates (usually X, Y, Z or X, Y, TWT)
    and trace or inter-trace positions on a seismic lattice.

    :ivar crossline_coordinates: The sequence of trace or inter-trace
        crossline positions that correspond to the geometry coordinates.
        BUSINESS RULE: Both sequences must be in the same order.
    :ivar inline_coordinates: The sequence of trace or inter-trace
        inline positions that correspond to the geometry coordinates.
        BUSINESS RULE: Both sequences must be in the same order.
    :ivar vertical_coordinates: The sequence of vertical sample or
        inter-sample positions that corresponds to the geometry
        coordinates. BUSINESS RULE: Sequence must be in the same order
        as the two previous ones.
    """

    class Meta:
        name = "Seismic3dCoordinates"

    crossline_coordinates: Optional[AbstractFloatingPointArray] = field(
        default=None,
        metadata={
            "name": "CrosslineCoordinates",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        },
    )
    inline_coordinates: Optional[AbstractFloatingPointArray] = field(
        default=None,
        metadata={
            "name": "InlineCoordinates",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        },
    )
    vertical_coordinates: Optional[AbstractFloatingPointArray] = field(
        default=None,
        metadata={
            "name": "VerticalCoordinates",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        },
    )


@dataclass
class SinglePointGeometry(AbstractGeometry):
    """
    The geometry of a single point defined by its location in the local CRS.
    """

    point3d: Optional[Point3D] = field(
        default=None,
        metadata={
            "name": "Point3d",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        },
    )


@dataclass
class SplitFaces:
    """Optional construction used to introduce additional faces created by split
    nodes.

    Used to represent complex geometries, e.g., for stair-step grids and
    reverse faults.

    :ivar count: Number of additional split faces. Count must be
        positive.
    :ivar parent_face_indices: Parent unsplit face index for each of the
        additional split faces.
    :ivar cell_per_split_face: Cell index for each split face. Used to
        implicitly define cell geometry.
    :ivar split_edges:
    """

    count: Optional[int] = field(
        default=None,
        metadata={
            "name": "Count",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
            "min_inclusive": 1,
        },
    )
    parent_face_indices: Optional[AbstractIntegerArray] = field(
        default=None,
        metadata={
            "name": "ParentFaceIndices",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        },
    )
    cell_per_split_face: Optional[AbstractIntegerArray] = field(
        default=None,
        metadata={
            "name": "CellPerSplitFace",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        },
    )
    split_edges: Optional[SplitEdges] = field(
        default=None,
        metadata={
            "name": "SplitEdges",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        },
    )


@dataclass
class StratigraphicIntervalBoundary(MarkerBoundary):
    """
    This represents a stratigraphic boundary between two intervals.

    :ivar contact_conformable_above: This is an optional boolean
        indicating that the relationship between the boundary and the
        unit above is conformable. It is typically used as a placeholder
        for the interpreter to put some information before the
        association with an organization is made.
    :ivar contact_conformable_below: This is an optional boolean
        indicating that the relationship between the boundary and the
        unit below is conformable. It is typically used as a placeholder
        for the interpreter to put some information before the
        association with an organization is made.
    """

    contact_conformable_above: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ContactConformableAbove",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        },
    )
    contact_conformable_below: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ContactConformableBelow",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        },
    )


@dataclass
class UniformSubnodePatch(SubnodePatch):
    """
    Use this subnode construction if the number of subnodes is the same for every
    object, e.g., 3 subnodes per edge for all edges.

    :ivar subnode_count_per_object: Number of subnodes per object, with
        the same number for each of this data-object kind in the grid.
    """

    subnode_count_per_object: Optional[int] = field(
        default=None,
        metadata={
            "name": "SubnodeCountPerObject",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
            "min_inclusive": 1,
        },
    )


@dataclass
class VariableSubnodePatch(SubnodePatch):
    """
    If the number of subnodes per data-object are variable for each data-object,
    use this subnode construction.

    :ivar object_indices: Indices of the selected data-objects
    :ivar subnode_count_per_selected_object: Number of subnodes per
        selected data-object.
    """

    object_indices: Optional[AbstractIntegerArray] = field(
        default=None,
        metadata={
            "name": "ObjectIndices",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        },
    )
    subnode_count_per_selected_object: Optional[AbstractIntegerArray] = field(
        default=None,
        metadata={
            "name": "SubnodeCountPerSelectedObject",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        },
    )


@dataclass
class VolumeRegion:
    """
    The volume within a shell.
    """

    internal_shells: List[VolumeShell] = field(
        default_factory=list,
        metadata={
            "name": "InternalShells",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        },
    )
    external_shell: Optional[VolumeShell] = field(
        default=None,
        metadata={
            "name": "ExternalShell",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        },
    )
    represents: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "Represents",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        },
    )


@dataclass
class WellboreFrameRepresentation(AbstractRepresentation):
    """Representation of a wellbore that is organized along a wellbore trajectory
    by its MD values.

    RESQML uses MD values to associate properties on points and to
    organize association of properties on intervals between MD points.
    For this particular representation a WITSML v2 Wellbore is
    considered as a RESQML Technical Feature, meaning that the WITSML v2
    Wellbore can be used as the represented data object for this
    representation.

    :ivar node_count: Number of nodes. Must be positive.
    :ivar node_md: MD values for each node. BUSINESS RULE: MD values and
        UOM must be consistent with the trajectory representation.
    :ivar witsml_log: The reference to the equivalent WITSML well log.
    :ivar trajectory:
    :ivar cell_fluid_phase_units:
    :ivar interval_stratigraphic_units:
    """

    class Meta:
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"

    node_count: Optional[int] = field(
        default=None,
        metadata={
            "name": "NodeCount",
            "type": "Element",
            "required": True,
            "min_inclusive": 1,
        },
    )
    node_md: Optional[AbstractFloatingPointArray] = field(
        default=None,
        metadata={
            "name": "NodeMd",
            "type": "Element",
            "required": True,
        },
    )
    witsml_log: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "WitsmlLog",
            "type": "Element",
        },
    )
    trajectory: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "Trajectory",
            "type": "Element",
            "required": True,
        },
    )
    cell_fluid_phase_units: Optional[CellFluidPhaseUnits] = field(
        default=None,
        metadata={
            "name": "CellFluidPhaseUnits",
            "type": "Element",
        },
    )
    interval_stratigraphic_units: List[IntervalStratigraphicUnits] = field(
        default_factory=list,
        metadata={
            "name": "IntervalStratigraphicUnits",
            "type": "Element",
        },
    )


@dataclass
class WellboreInterpretation(AbstractFeatureInterpretation):
    """Contains the data describing an opinion of a borehole.

    This interpretation is relative to one particular well trajectory.

    :ivar is_drilled: Used to indicate that this wellbore has been, or
        is being, drilled, as opposed to planned wells. One wellbore
        feature may have multiple wellbore interpretations. - For
        updated drilled trajectories, use IsDrilled=TRUE. - For planned
        trajectories, use IsDrilled=FALSE used.
    """

    class Meta:
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"

    is_drilled: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsDrilled",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class WellboreIntervalSet(AbstractRepresentation):
    class Meta:
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"

    interval_boundaries: List[MarkerBoundary] = field(
        default_factory=list,
        metadata={
            "name": "IntervalBoundaries",
            "type": "Element",
        },
    )
    marker_interval: List[MarkerInterval] = field(
        default_factory=list,
        metadata={
            "name": "MarkerInterval",
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass
class AbstractGeologicUnitOrganizationInterpretation(
    AbstractOrganizationInterpretation
):
    """The main class that defines the relationships between the stratigraphic
    units and provides the stratigraphic hierarchy of the Earth.

    BUSINESS RULE: A stratigraphic organization must be in a ranked order from a lower rank to an upper rank. For example, it is possible to find previous unit containment relationships between several ranks.
    """

    ascending_ordering_criteria: Optional[OrderingCriteria] = field(
        default=None,
        metadata={
            "name": "AscendingOrderingCriteria",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        },
    )


@dataclass
class AbstractGridGeometry(PointGeometry):
    """
    Grid geometry described by means of points attached to nodes and additional
    optional points which may be attached to other indexable elements of the grid
    representation.
    """

    additional_grid_points: List[AdditionalGridPoints] = field(
        default_factory=list,
        metadata={
            "name": "AdditionalGridPoints",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        },
    )


@dataclass
class AbstractParentWindow:
    """Parent window specification, organized according to the topology of the
    parent grid.

    In addition to a window specification, for grids with I, J, and/or K
    coordinates, the parentage construction includes a regridding
    description that covers grid refinement, coarsening, or any
    combination of the two.
    """

    cell_overlap: Optional[CellOverlap] = field(
        default=None,
        metadata={
            "name": "CellOverlap",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        },
    )


@dataclass
class AbstractSeismicSurveyFeature(AbstractTechnicalFeature):
    """An organization of seismic lines. For the context of RESQML, a seismic
    survey does not refer to any vertical dimension information, but only areally
    at shot point locations or common midpoint gathers. The seismic traces, if
    needed by reservoir models, are transferred in an industry standard format such
    as SEGY.

    RESQML supports these basic types of seismic surveys:
    - seismic lattice (organization of the traces for the 3D acquisition and processing phases).
    - seismic line (organization of the traces for the 2D acquisition and processing phases).
    Additionally, these seismic lattices and seismic lines can be aggregated into sets.
    """


@dataclass
class AbstractSurfaceFrameworkRepresentation(RepresentationSetRepresentation):
    """Parent class for a sealed or non-sealed surface framework representation.

    Each one instantiates a representation set representation. The
    difference between the sealed and non-sealed frameworks is that, in
    the non-sealed case, we do not have all of the contact
    representations, or we have all of the contacts but they are not all
    sealed.
    """

    contact_identity: List[ContactIdentity] = field(
        default_factory=list,
        metadata={
            "name": "ContactIdentity",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        },
    )


@dataclass
class BlockedWellboreRepresentation(WellboreFrameRepresentation):
    """
    The information that allows you to locate, on one or several grids (existing or
    planned), the intersection of volume (cells) and surface (faces) elements with
    a wellbore trajectory (existing or planned).
    """

    class Meta:
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"

    interval_grid_cells: Optional[IntervalGridCells] = field(
        default=None,
        metadata={
            "name": "IntervalGridCells",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class BooleanProperty(AbstractValuesProperty):
    """Information specific to one Boolean property.

    Used to capture a choice between 2 and only 2 possible values/states
    for each indexable element of a data object, for example,
    identifying active cells of a grid..
    """

    class Meta:
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class CommentProperty(AbstractValuesProperty):
    """Information specific to one comment property.

    Used to capture comments or annotations associated with a given
    element type in a data-object, for example, associating comments on
    the specific location of a well path.

    :ivar language: Identify the language (e.g., US English or French)
        of the string. It is recommended that language names conform to
        ISO 639.
    """

    class Meta:
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"

    language: Optional[str] = field(
        default=None,
        metadata={
            "name": "Language",
            "type": "Element",
            "max_length": 64,
        },
    )


@dataclass
class ContinuousProperty(AbstractValuesProperty):
    """Most common type of property used for storing rock or fluid attributes; all
    are represented as doubles.

    Statistics about values such as maximum and minimum can be found in the statistics of each ValueForPatch.
    BUSINESS RULE: It also contains a unit of measure, which can be different from the unit of measure of its property type, but it must be convertible into this unit.

    :ivar uom: Unit of measure for the property.
    :ivar custom_unit_dictionary:
    """

    class Meta:
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"

    uom: Optional[Union[LegacyUnitOfMeasure, UnitOfMeasure, str]] = field(
        default=None,
        metadata={
            "name": "Uom",
            "type": "Element",
            "required": True,
            "pattern": r".*:.*",
        },
    )
    custom_unit_dictionary: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "CustomUnitDictionary",
            "type": "Element",
        },
    )


@dataclass
class ContourLineSetInformation(AbstractGraphicalInformation):
    """
    Information about contour lines between regions having different ranges of
    values (elevation or depth mostly).

    :ivar display_label_on_major_line: Indicator to display the contour
        line value on major lines. To differentiate minor and major
        lines, see ShowMajorLineEvery.
    :ivar display_label_on_minor_line: Indicator to display the contour
        line value on minor lines. To differentiate minor and major
        lines, see ShowMajorLineEvery.
    :ivar increment: The absolute incremented value between two
        consecutive minor contour lines.
    :ivar major_line_graphical_information: Graphical information of
        major lines.
    :ivar minor_line_graphical_information: Graphical information of
        minor lines.
    :ivar show_major_line_every: Allows to regularly promote some minor
        lines to major lines.
    :ivar value_vector_index: Especially useful for vectorial property
        and for geometry.
    """

    display_label_on_major_line: Optional[bool] = field(
        default=None,
        metadata={
            "name": "DisplayLabelOnMajorLine",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        },
    )
    display_label_on_minor_line: Optional[bool] = field(
        default=None,
        metadata={
            "name": "DisplayLabelOnMinorLine",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        },
    )
    increment: Optional[float] = field(
        default=None,
        metadata={
            "name": "Increment",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        },
    )
    major_line_graphical_information: Optional[
        GraphicalInformationForEdges
    ] = field(
        default=None,
        metadata={
            "name": "MajorLineGraphicalInformation",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        },
    )
    minor_line_graphical_information: Optional[
        GraphicalInformationForEdges
    ] = field(
        default=None,
        metadata={
            "name": "MinorLineGraphicalInformation",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        },
    )
    show_major_line_every: Optional[int] = field(
        default=None,
        metadata={
            "name": "ShowMajorLineEvery",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        },
    )
    value_vector_index: Optional[int] = field(
        default=None,
        metadata={
            "name": "ValueVectorIndex",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        },
    )


@dataclass
class CulturalFeature(AbstractTechnicalFeature):
    """
    Identifies a frontier or boundary in the earth model that is not a geological
    feature but an arbitrary geographic/geometric surface used to delineate the
    boundary of the model.
    """

    class Meta:
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"

    cultural_feature_kind: Optional[Union[CulturalFeatureKind, str]] = field(
        default=None,
        metadata={
            "name": "CulturalFeatureKind",
            "type": "Element",
            "required": True,
            "pattern": r".*:.*",
        },
    )


@dataclass
class DiscreteProperty(AbstractValuesProperty):
    """Contains discrete integer values; typically used to store any type of index.

    Statistics about values such as maximum and minimum can be found in
    the statistics of each ValueForPatch.
    """

    class Meta:
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"

    category_lookup: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "CategoryLookup",
            "type": "Element",
        },
    )


@dataclass
class FaultInterpretation(BoundaryFeatureInterpretation):
    """A general term for designating a boundary feature intepretation that
    corresponds to a discontinuity having a tectonic origin, identified at mapping
    or outcrop scale.

    Fault may designate true faults but also thrust surfaces. A thrust
    surface  is specified as a FaultInterpretation whose FaultThrow kind
    is "thrust" and which has the attributes: is Listric = 0,
    MaximumThrow = 0.

    :ivar dip_direction_north_reference_kind: If not set (absent), the
        NorthReferenceKind is Grid North.
    :ivar is_listric: Indicates if the normal fault is listric or not.
        BUSINESS RULE: Must be present if the fault is normal. Must not
        be present if the fault is not normal.
    :ivar is_sealed:
    :ivar maximum_throw:
    :ivar mean_azimuth: For this element, "mean" means "representative";
        it is not a mathematically derived mean.
    :ivar mean_dip: For this element, "mean" means "representative"; it
        is not a mathematically derived mean. It is relative to
        horizontal however horizontal is defined by the CRS.
    :ivar throw_interpretation:
    """

    class Meta:
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"

    dip_direction_north_reference_kind: Optional[NorthReferenceKind] = field(
        default=None,
        metadata={
            "name": "DipDirectionNorthReferenceKind",
            "type": "Element",
        },
    )
    is_listric: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsListric",
            "type": "Element",
        },
    )
    is_sealed: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsSealed",
            "type": "Element",
        },
    )
    maximum_throw: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "MaximumThrow",
            "type": "Element",
        },
    )
    mean_azimuth: Optional[PlaneAngleMeasure] = field(
        default=None,
        metadata={
            "name": "MeanAzimuth",
            "type": "Element",
        },
    )
    mean_dip: Optional[PlaneAngleMeasure] = field(
        default=None,
        metadata={
            "name": "MeanDip",
            "type": "Element",
        },
    )
    throw_interpretation: List[FaultThrow] = field(
        default_factory=list,
        metadata={
            "name": "ThrowInterpretation",
            "type": "Element",
        },
    )


@dataclass
class FluidBoundaryInterpretation(BoundaryFeatureInterpretation):
    """A boundary (usually a plane or a set of planes) separating two fluid phases,
    such as a gas-oil contact (GOC), a water-oil contact (WOC), a gas-oil contact
    (GOC), or others.

    For types, see FluidContact.

    :ivar fluid_contact: The kind of contact of this boundary.
    """

    class Meta:
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"

    fluid_contact: Optional[FluidContact] = field(
        default=None,
        metadata={
            "name": "FluidContact",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class GeobodyBoundaryInterpretation(BoundaryFeatureInterpretation):
    """
    Contains the data describing an opinion about the characterization of a geobody
    BoundaryFeature, and it includes the attribute boundary relation.

    :ivar boundary_relation: Characterizes the stratigraphic
        relationships of a horizon with the stratigraphic units that its
        bounds.
    :ivar is_conformable_above: Optional Boolean flag to indicate that
        the geobody boundary interpretation is conformable above.
    :ivar is_conformable_below: Optional Boolean flag to indicate that
        the geobody boundary interpretation is conformable below.
    """

    class Meta:
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"

    boundary_relation: List[str] = field(
        default_factory=list,
        metadata={
            "name": "BoundaryRelation",
            "type": "Element",
        },
    )
    is_conformable_above: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsConformableAbove",
            "type": "Element",
        },
    )
    is_conformable_below: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsConformableBelow",
            "type": "Element",
        },
    )


@dataclass
class GeobodyInterpretation(GeologicUnitInterpretation):
    """A volume of rock that is identified based on some specific attribute, like
    its mineral content or other physical characteristic.

    Unlike stratigraphic or phase units, there is no associated time or
    fluid content semantic.
    """

    class Meta:
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class Graph2DRepresentation(AbstractRepresentation):
    """
    The geometry of a single point defined by its location in the local CRS.
    """

    class Meta:
        name = "Graph2dRepresentation"

    edges: Optional[AbstractIntegerArray] = field(
        default=None,
        metadata={
            "name": "Edges",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        },
    )
    is_directed: Optional[bool] = field(
        default=None,
        metadata={
            "name": "isDirected",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        },
    )
    geometry: Optional[PointGeometry] = field(
        default=None,
        metadata={
            "name": "Geometry",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        },
    )


@dataclass
class Grid2DRepresentation(AbstractSurfaceRepresentation):
    """Representation based on a 2D grid.

    For definitions of slowest and fastest axes of the array, see
    Grid2dPatch.
    """

    class Meta:
        name = "Grid2dRepresentation"
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"

    fastest_axis_count: Optional[int] = field(
        default=None,
        metadata={
            "name": "FastestAxisCount",
            "type": "Element",
            "required": True,
            "min_inclusive": 1,
        },
    )
    slowest_axis_count: Optional[int] = field(
        default=None,
        metadata={
            "name": "SlowestAxisCount",
            "type": "Element",
            "required": True,
            "min_inclusive": 1,
        },
    )
    geometry: Optional[PointGeometry] = field(
        default=None,
        metadata={
            "name": "Geometry",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class HorizonInterpretation(BoundaryFeatureInterpretation):
    """
    An interpretation of a horizon, which optionally provides stratigraphic
    information on BoundaryRelation, HorizonStratigraphicRole,
    SequenceStratigraphysurface .

    :ivar is_conformable_above: Optional Boolean flag to indicate that
        the horizon interpretation is conformable above.
    :ivar is_conformable_below: Optional Boolean flag to indicate that
        the horizon interpretation is conformable below.
    :ivar stratigraphic_role:
    :ivar sequence_stratigraphy_surface:
    """

    class Meta:
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"

    is_conformable_above: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsConformableAbove",
            "type": "Element",
        },
    )
    is_conformable_below: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsConformableBelow",
            "type": "Element",
        },
    )
    stratigraphic_role: List[StratigraphicRole] = field(
        default_factory=list,
        metadata={
            "name": "StratigraphicRole",
            "type": "Element",
        },
    )
    sequence_stratigraphy_surface: Optional[
        Union[SequenceStratigraphySurfaceKind, str]
    ] = field(
        default=None,
        metadata={
            "name": "SequenceStratigraphySurface",
            "type": "Element",
            "pattern": r".*:.*",
        },
    )


@dataclass
class HorizontalPlaneGeometry(AbstractPlaneGeometry):
    """
    Defines the infinite geometry of a horizontal plane provided by giving its
    unique Z value.
    """

    coordinate: Optional[float] = field(
        default=None,
        metadata={
            "name": "Coordinate",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        },
    )


@dataclass
class ParametricLineFromRepresentationGeometry(AbstractParametricLineGeometry):
    """The parametric line extracted from an existing representation.

    BUSINESS RULE: The supporting representation must have pillars or lines as indexable elements.

    :ivar line_index_on_supporting_representation: The line index of the
        selected line in the supporting representation. For a column-
        layer grid, the parametric lines follow the indexing of the
        pillars.
    :ivar supporting_representation:
    """

    line_index_on_supporting_representation: Optional[int] = field(
        default=None,
        metadata={
            "name": "LineIndexOnSupportingRepresentation",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
            "min_inclusive": 0,
        },
    )
    supporting_representation: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "SupportingRepresentation",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        },
    )


@dataclass
class ParametricLineGeometry(AbstractParametricLineGeometry):
    """Defines a parametric line of any kind.

    For more information on the supported parametric lines, see
    ParametricLineArray.

    :ivar control_point_parameters: An array of explicit control point
        parameters for the control points on the parametric line.
        BUSINESS RULE: The size MUST match the number of control points.
        BUSINESS RULE: The parametric values MUST be strictly
        monotonically increasing on the parametric line.
    :ivar control_points: An array of 3D points for the control points
        on the parametric line.
    :ivar knot_count: Number of spline knots in the parametric line.
    :ivar line_kind_index: Integer indicating the parametric line kind 0
        for vertical 1 for linear spline 2 for natural cubic spline 3
        for cubic spline 4 for z linear cubic spline 5 for minimum-
        curvature spline (-1) for null: no line
    :ivar tangent_vectors: An optional array of tangent vectors for each
        control point on the cubic and minimum-curvature parametric
        lines. Used only if tangent vectors are present. If a tangent
        vector is missing, then it is computed in the same fashion as
        for a natural cubic spline. Specifically, to obtain the tangent
        at internal knots, the control points are fit by a quadratic
        function with the two adjacent control points. At edge knots,
        the second derivative vanishes.
    """

    control_point_parameters: Optional[AbstractFloatingPointArray] = field(
        default=None,
        metadata={
            "name": "ControlPointParameters",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        },
    )
    control_points: Optional[AbstractPoint3DArray] = field(
        default=None,
        metadata={
            "name": "ControlPoints",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        },
    )
    knot_count: Optional[int] = field(
        default=None,
        metadata={
            "name": "KnotCount",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
            "min_inclusive": 1,
        },
    )
    line_kind_index: Optional[int] = field(
        default=None,
        metadata={
            "name": "LineKindIndex",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        },
    )
    tangent_vectors: Optional[AbstractPoint3DArray] = field(
        default=None,
        metadata={
            "name": "TangentVectors",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        },
    )


@dataclass
class PlaneSetRepresentation(AbstractSurfaceRepresentation):
    """Defines a plane representation, which can be made up of multiple patches.

    Commonly represented features are fluid contacts or frontiers. Common geometries of this representation are titled or horizontal planes.
    BUSINESS RULE: If the plane representation is made up of multiple patches, then you must specify the outer rings for each plane patch.
    """

    class Meta:
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"

    planes: List[AbstractPlaneGeometry] = field(
        default_factory=list,
        metadata={
            "name": "Planes",
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass
class PointSetRepresentation(AbstractRepresentation):
    """A representation that consists of one or more node patches.

    Each node patch is an array of XYZ coordinates for the 3D points.
    There is no implied linkage between the multiple patches.
    """

    class Meta:
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"

    node_patch_geometry: List[PointGeometry] = field(
        default_factory=list,
        metadata={
            "name": "NodePatchGeometry",
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass
class PolylineRepresentation(AbstractRepresentation):
    """A representation made up of a single polyline or "polygonal chain", which
    may be closed or not.

    Definition from Wikipedia (http://en.wikipedia.org/wiki/Piecewise_linear_curve):
    A polygonal chain, polygonal curve, polygonal path, or piecewise linear curve, is a connected series of line segments. More formally, a polygonal chain P is a curve specified by a sequence of points \\scriptstyle(A_1, A_2, \\dots, A_n) called its vertices so that the curve consists of the line segments connecting the consecutive vertices.
    In computer graphics a polygonal chain is called a polyline and is often used to approximate curved paths.
    BUSINESS RULE: To record a polyline the writer software must give the values of the geometry of each node in an order corresponding to the logical series of segments (edges). The geometry of a polyline must be a 1D array of points.
    A simple polygonal chain is one in which only consecutive (or the first and the last) segments intersect and only at their endpoints.
    A closed polygonal chain (isClosed=True) is one in which the first vertex coincides with the last one, or the first and the last vertices are connected by a line segment.
    """

    class Meta:
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"

    line_role: Optional[Union[LineRole, str]] = field(
        default=None,
        metadata={
            "name": "LineRole",
            "type": "Element",
            "pattern": r".*:.*",
        },
    )
    is_closed: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsClosed",
            "type": "Element",
            "required": True,
        },
    )
    node_patch_geometry: Optional[PointGeometry] = field(
        default=None,
        metadata={
            "name": "NodePatchGeometry",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class PolylineSetPatch:
    """A Patch containing a set of polylines. For performance reasons, the geometry
    of each Patch is described in only one 1D array of 3D points, which aggregates
    the nodes of all the polylines together. To be able to separate the polyline
    descriptions, additional information is added about the type of each polyline
    (closed or not) and the number of 3D points (node count) of each polyline.

    This additional information is contained in two arrays, which are associated with each polyline set patch. The dimension of these arrays is the number of polylines gathered in one polyline set patch.
    - The first array contains a Boolean for each polyline (closed or not closed).
    - The second array contains the count of nodes for each polyline.

    :ivar node_count: Total number of nodes. BUSINESS RULE: Should be
        equal to the sum of the number of nodes per polyline.
    :ivar interval_count: Total number of intervals. BUSINESS RULE:
        Should be equal to the sum of the count of intervals per
        polyline.
    :ivar node_count_per_polyline: The first number in the list defines
        the node count for the first polyline in the polyline set patch.
        The second number in the list defines the node count for the
        second polyline in the polyline set patch. etc.
    :ivar closed_polylines: Indicates whether a polyline is closed. If
        closed, then the interval count for that polyline is equal to
        the node count. If open, then the interval count for that
        polyline is one less than the node count.
    :ivar interval_grid_cells:
    :ivar geometry:
    """

    node_count: Optional[int] = field(
        default=None,
        metadata={
            "name": "NodeCount",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
            "min_inclusive": 1,
        },
    )
    interval_count: Optional[int] = field(
        default=None,
        metadata={
            "name": "IntervalCount",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
            "min_inclusive": 0,
        },
    )
    node_count_per_polyline: Optional[AbstractIntegerArray] = field(
        default=None,
        metadata={
            "name": "NodeCountPerPolyline",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        },
    )
    closed_polylines: Optional[AbstractBooleanArray] = field(
        default=None,
        metadata={
            "name": "ClosedPolylines",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        },
    )
    interval_grid_cells: Optional[IntervalGridCells] = field(
        default=None,
        metadata={
            "name": "IntervalGridCells",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        },
    )
    geometry: Optional[PointGeometry] = field(
        default=None,
        metadata={
            "name": "Geometry",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        },
    )


@dataclass
class ReservoirCompartmentInterpretation(GeologicUnitInterpretation):
    """A portion of a reservoir rock which is differentiated laterally from other
    portions of the same reservoir stratum.

    This differentiation could be due to being in a different fault
    block or a different channel or other stratigraphic or structural
    aspect. A reservoir compartment may or may not be in contact with
    other reservoir compartments.
    """


@dataclass
class RockFluidOrganizationInterpretation(AbstractOrganizationInterpretation):
    """This class describes the organization of geological reservoir, i.e., of an
    interconnected network of porous and permeable rock units, containing an
    accumulation of economic fluids, such as oil and gas.

    A reservoir is normally enveloped by rock and fluid barriers and
    contains a single natural pressure system.
    """

    class Meta:
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"

    rock_fluid_unit: List[DataObjectReference] = field(
        default_factory=list,
        metadata={
            "name": "RockFluidUnit",
            "type": "Element",
        },
    )


@dataclass
class RockFluidUnitInterpretation(GeologicUnitInterpretation):
    """
    A type of rock fluid feature-interpretation, this class identifies a rock fluid
    unit interpretation by its phase.
    """

    class Meta:
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"

    phase: Optional[Phase] = field(
        default=None,
        metadata={
            "name": "Phase",
            "type": "Element",
        },
    )


@dataclass
class SealedVolumeFrameworkRepresentation(RepresentationSetRepresentation):
    """A strict boundary representation (BREP), which represents the volume region
    by assembling together shells.

    BUSINESS RULE: The sealed structural framework must be part of the same earth model as this sealed volume framework.
    """

    class Meta:
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"

    based_on: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "BasedOn",
            "type": "Element",
            "required": True,
        },
    )
    regions: List[VolumeRegion] = field(
        default_factory=list,
        metadata={
            "name": "Regions",
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass
class SeismicWellboreFrameRepresentation(WellboreFrameRepresentation):
    """The interpretation of this representation must be a WellboreInterpretation.

    The acquisition information such as the time kind (e.g., TWT vs OWT
    for example) or survey acquisition type (e.g., checkshot vs VSP)
    should be captured by the associated acquisition activity.

    :ivar node_time_values: BUSINESS RULE: Count must be  equal to the
        inherited NodeCount. The direction of the supporting axis is
        given by the LocalTime3dCrs itself. It is necessary to get this
        information to know what means positive or negative values. The
        values are given with respect to the SeismicReferenceDatum. The
        UOM is the one specified in the LocalTime3dCrs.
    :ivar seismic_reference_datum: This is the Z value where the seismic
        time is equal to zero for this survey wellbore frame. The
        direction of the supporting axis is given by the LocalTime3dCrs
        of the associated wellbore trajectory. It is necessary to get
        the information to know what means a positive or a negative
        value. The value is given with respect to the ZOffset of the
        LocalDepth3dCrs of the associated wellbore trajectory. The UOM
        is the one specified in the LocalDepth3dCrs of the associated
        wellbore trajectory.
    :ivar weathering_velocity: The UOM is composed by: UOM of the
        LocalDepth3dCrs of the associated wellbore frame trajectory /
        UOM of the associated LocalTime3dCrs Sometimes also called
        seismic velocity replacement.
    :ivar tvd_information:
    :ivar correction_information:
    :ivar local_time3d_crs:
    """

    class Meta:
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"

    node_time_values: Optional[AbstractFloatingPointArray] = field(
        default=None,
        metadata={
            "name": "NodeTimeValues",
            "type": "Element",
            "required": True,
        },
    )
    seismic_reference_datum: Optional[float] = field(
        default=None,
        metadata={
            "name": "SeismicReferenceDatum",
            "type": "Element",
            "required": True,
        },
    )
    weathering_velocity: Optional[float] = field(
        default=None,
        metadata={
            "name": "WeatheringVelocity",
            "type": "Element",
            "required": True,
        },
    )
    tvd_information: Optional[TvdInformation] = field(
        default=None,
        metadata={
            "name": "TvdInformation",
            "type": "Element",
        },
    )
    correction_information: Optional[CorrectionInformation] = field(
        default=None,
        metadata={
            "name": "CorrectionInformation",
            "type": "Element",
        },
    )
    local_time3d_crs: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "LocalTime3dCrs",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class SplitNodePatch:
    """Optional construction used to introduce additional nodes on coordinate
    lines.

    Used to represent complex geometries, e.g., for stair-step grids and reverse faults.
    BUSINESS RULE: Patch index must be positive because a patch index of 0 refers to the fundamental column-layer coordinate line nodes.

    :ivar count: Number of additional split nodes. Count must be
        positive.
    :ivar parent_node_indices: Parent coordinate line node index for
        each of the split nodes. Used to implicitly define cell
        geometry.
    :ivar cells_per_split_node: Cell indices for each of the split
        nodes. Used to implicitly define cell geometry. List-of-lists
        construction used to support split nodes shared between multiple
        cells.
    :ivar split_faces:
    """

    count: Optional[int] = field(
        default=None,
        metadata={
            "name": "Count",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
            "min_inclusive": 1,
        },
    )
    parent_node_indices: Optional[AbstractIntegerArray] = field(
        default=None,
        metadata={
            "name": "ParentNodeIndices",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        },
    )
    cells_per_split_node: Optional[JaggedArray] = field(
        default=None,
        metadata={
            "name": "CellsPerSplitNode",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        },
    )
    split_faces: Optional[SplitFaces] = field(
        default=None,
        metadata={
            "name": "SplitFaces",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        },
    )


@dataclass
class StratigraphicUnitInterpretation(GeologicUnitInterpretation):
    """A volume of rock of identifiable origin and relative age range that is
    defined by the distinctive and dominant, easily mapped and recognizable
    features that characterize it (petrographic, lithologic, paleontologic,
    paleomagnetic or chemical features).

    Some stratigraphic units (chronostratigraphic units) have a
    GeneticBoundaryBasedTimeInterval (between its ChronoTop and
    ChronoBottom) defined by a BoundaryFeatureInterpretation. A
    stratigraphic unit has no direct link to its physical top and bottom
    limits. These physical limits are only defined as contacts between
    StratigraphicUnitInterpretations defined within a
    StratigraphicOrganizationInterpretation.

    :ivar deposition_mode: BUSINESS RULE: The deposition mode for a
        geological unit MUST be consistent with the boundary relations
        of a genetic boundary. If it is not, then the boundary relation
        declaration is retained.
    :ivar max_thickness:
    :ivar min_thickness:
    :ivar stratigraphic_role:
    """

    class Meta:
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"

    deposition_mode: Optional[DepositionMode] = field(
        default=None,
        metadata={
            "name": "DepositionMode",
            "type": "Element",
        },
    )
    max_thickness: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "MaxThickness",
            "type": "Element",
        },
    )
    min_thickness: Optional[LengthMeasure] = field(
        default=None,
        metadata={
            "name": "MinThickness",
            "type": "Element",
        },
    )
    stratigraphic_role: Optional[StratigraphicRole] = field(
        default=None,
        metadata={
            "name": "StratigraphicRole",
            "type": "Element",
        },
    )


@dataclass
class StreamlinesFeature(AbstractTechnicalFeature):
    """Specification of the vector field upon which the streamlines are based.

    Streamlines are commonly used to trace the flow of phases (water /
    oil / gas / total) based upon their flux at a specified time. They
    may also be used for trace components for compositional simulation,
    e.g., CO2, or temperatures for thermal simulation. The flux
    enumeration provides support for the most usual cases with provision
    for extensions to other fluxes.

    :ivar flux: Specification of the streamline flux, drawn from the
        enumeration.
    :ivar time_index:
    """

    class Meta:
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"

    flux: Optional[Union[StreamlineFlux, str]] = field(
        default=None,
        metadata={
            "name": "Flux",
            "type": "Element",
            "required": True,
            "pattern": r".*:.*",
        },
    )
    time_index: Optional[TimeIndex] = field(
        default=None,
        metadata={
            "name": "TimeIndex",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class StructuralOrganizationInterpretation(AbstractOrganizationInterpretation):
    """One of the main types of RESQML organizations, this class gathers boundary
    interpretations (e.g., horizons, faults and fault networks) plus frontier
    features and their relationships (contacts interpretations), which when taken
    together define the structure of a part of the earth.

    IMPLEMENTATION RULE: Two use cases are presented:
    1. If the relative age or apparent depth between faults and horizons is unknown, the writer must provide all individual faults within the UnorderedFaultCollection FeatureInterpretationSet.
    2. Else, the writer must provide individual faults and fault collections within the OrderedBoundaryFeatureInterpretation list.
    BUSINESS RULE: Two use cases are processed:
    1. If relative age or apparent depth between faults and horizons are unknown, the writer must provides all individual faults within the UnorderedFaultCollection FeatureInterpretationSet.
    2. Else, individual faults and fault collections are provided within the OrderedBoundaryFeatureInterpretation list.

    :ivar ascending_ordering_criteria:
    :ivar bottom_frontier: BUSINESS RULE: It either points to a
        CulturalFeature whose Kind is model frontier or to a
        BoundaryFeatureInterpretation if the frontier is actually a
        geologic surface
    :ivar top_frontier: BUSINESS RULE: It either points to a
        CulturalFeature whose Kind is model frontier or to a
        BoundaryFeatureInterpretation if the frontier is actually a
        geologic surface
    :ivar sides: BUSINESS RULE: It either points to a CulturalFeature
        whose Kind is model frontier or to a
        BoundaryFeatureInterpretation if the frontier is actually a
        geologic surface
    :ivar ordered_boundary_feature_interpretation:
    """

    class Meta:
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"

    ascending_ordering_criteria: Optional[OrderingCriteria] = field(
        default=None,
        metadata={
            "name": "AscendingOrderingCriteria",
            "type": "Element",
            "required": True,
        },
    )
    bottom_frontier: List[DataObjectReference] = field(
        default_factory=list,
        metadata={
            "name": "BottomFrontier",
            "type": "Element",
        },
    )
    top_frontier: List[DataObjectReference] = field(
        default_factory=list,
        metadata={
            "name": "TopFrontier",
            "type": "Element",
        },
    )
    sides: List[DataObjectReference] = field(
        default_factory=list,
        metadata={
            "name": "Sides",
            "type": "Element",
        },
    )
    ordered_boundary_feature_interpretation: List[
        BoundaryFeatureInterpretationPlusItsRank
    ] = field(
        default_factory=list,
        metadata={
            "name": "OrderedBoundaryFeatureInterpretation",
            "type": "Element",
        },
    )


@dataclass
class SubnodeTopology:
    """
    Finite element subnode topology for an unstructured cell can be either variable
    or uniform, but not columnar.
    """

    variable_subnode_patch: List[VariableSubnodePatch] = field(
        default_factory=list,
        metadata={
            "name": "VariableSubnodePatch",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        },
    )
    uniform_subnode_patch: List[UniformSubnodePatch] = field(
        default_factory=list,
        metadata={
            "name": "UniformSubnodePatch",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        },
    )


@dataclass
class TiltedPlaneGeometry(AbstractPlaneGeometry):
    """
    Describes the geometry of a tilted (or potentially not tilted) plane from three
    points.
    """

    plane: List[ThreePoint3D] = field(
        default_factory=list,
        metadata={
            "name": "Plane",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "min_occurs": 1,
        },
    )


@dataclass
class TrianglePatch:
    """Patch made of triangles, where the number of triangles is given by the patch count.
    BUSINESS RULE: Within a patch, all the triangles must be contiguous.
    The patch contains:
    - Number of nodes within the triangulation and their locations.
    - 2D array describing the topology of the triangles.
    Two triangles that are connected may be in different patches.

    :ivar node_count:
    :ivar triangles: The triangles are a 2D array of non-negative
        integers with the dimensions 3 x numTriangles.
    :ivar split_edge_patch:
    :ivar geometry:
    """

    node_count: Optional[int] = field(
        default=None,
        metadata={
            "name": "NodeCount",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
            "min_inclusive": 0,
        },
    )
    triangles: Optional[AbstractIntegerArray] = field(
        default=None,
        metadata={
            "name": "Triangles",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        },
    )
    split_edge_patch: List[EdgePatch] = field(
        default_factory=list,
        metadata={
            "name": "SplitEdgePatch",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        },
    )
    geometry: Optional[PointGeometry] = field(
        default=None,
        metadata={
            "name": "Geometry",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        },
    )


@dataclass
class WellboreFeature(AbstractTechnicalFeature):
    """May refer to one of these:
    wellbore. A unique, oriented path from the bottom of a drilled borehole to the surface of the earth. The path must not overlap or cross itself.
    borehole. A hole excavated in the earth as a result of drilling or boring operations. The borehole may represent the hole of an entire wellbore (when no sidetracks are present), or a sidetrack extension. A borehole extends from an originating point (the surface location for the initial borehole or kickoff point for sidetracks) to a terminating (bottomhole) point.
    sidetrack. A borehole that originates in another borehole as opposed to originating at the surface."""

    class Meta:
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"

    witsml_wellbore: Optional[WitsmlWellWellbore] = field(
        default=None,
        metadata={
            "name": "WitsmlWellbore",
            "type": "Element",
        },
    )


@dataclass
class WellboreTrajectoryRepresentation(AbstractRepresentation):
    """Representation of a wellbore trajectory.

    For this particular representation a WITSML v2 Wellbore is
    considered as a RESQML Technical Feature, meaning that the WITSML v2
    Wellbore can be used as the represented data object for this
    representation.

    :ivar md_interval: The interval which represents the minimum and
        maximum values of measured depth for the trajectory. BUSINESS
        RULE: For purposes of the trajectory the MdDatum within the
        MdInterval is mandatory. BUSINESS RULE: The MdMin must be less
        than the MdMax within the MdInterval
    :ivar custom_unit_dictionary: If the unit of measure of the
        MdInterval is an extended value, this is a reference to an
        object containing the custom unit dictionary.
    :ivar md_domain: Indicates if the MD is either in "driller" domain
        or "logger" domain.
    :ivar witsml_trajectory: Pointer to the WITSML trajectory that is
        contained in the referenced wellbore. (For information about
        WITSML well and wellbore references, see the definition for
        RESQML technical feature, WellboreFeature).
    :ivar parent_intersection:
    :ivar geometry: Explicit geometry is not required for vertical wells
    """

    class Meta:
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"

    md_interval: Optional[MdInterval] = field(
        default=None,
        metadata={
            "name": "MdInterval",
            "type": "Element",
            "required": True,
        },
    )
    custom_unit_dictionary: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "CustomUnitDictionary",
            "type": "Element",
        },
    )
    md_domain: Optional[MdDomain] = field(
        default=None,
        metadata={
            "name": "MdDomain",
            "type": "Element",
        },
    )
    witsml_trajectory: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "WitsmlTrajectory",
            "type": "Element",
        },
    )
    parent_intersection: Optional[
        WellboreTrajectoryParentIntersection
    ] = field(
        default=None,
        metadata={
            "name": "ParentIntersection",
            "type": "Element",
        },
    )
    geometry: Optional[AbstractParametricLineGeometry] = field(
        default=None,
        metadata={
            "name": "Geometry",
            "type": "Element",
        },
    )


@dataclass
class AbstractGridRepresentation(AbstractRepresentation):
    """
    Abstract class for all grid representations.
    """

    cell_fluid_phase_units: Optional[CellFluidPhaseUnits] = field(
        default=None,
        metadata={
            "name": "CellFluidPhaseUnits",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        },
    )
    parent_window: Optional[AbstractParentWindow] = field(
        default=None,
        metadata={
            "name": "ParentWindow",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        },
    )
    interval_stratigraphic_units: Optional[IntervalStratigraphicUnits] = field(
        default=None,
        metadata={
            "name": "IntervalStratigraphicUnits",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        },
    )


@dataclass
class AbstractSeismicLineFeature(AbstractSeismicSurveyFeature):
    """Location of the line used in a 2D seismic acquisition.

    Defined by one lateral dimension: trace (lateral).
    To specify its location, the seismic feature can be associated with the seismic coordinates of the points of a representation.
    Represented by a PolylineRepresentation.
    """

    trace_labels: Optional[StringExternalArray] = field(
        default=None,
        metadata={
            "name": "TraceLabels",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        },
    )
    is_part_of: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "IsPartOf",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        },
    )


@dataclass
class CellParentWindow(AbstractParentWindow):
    """
    Parent window for ANY grid indexed as if it were an unstructured cell grid,
    i.e., using a 1D index.

    :ivar cell_indices: Cell indices that list the cells in the parent
        window. BUSINESS RULE: The ratio of fine to coarse cell counts
        must be an integer for each coarse cell.
    :ivar parent_grid_representation:
    """

    cell_indices: Optional[AbstractIntegerArray] = field(
        default=None,
        metadata={
            "name": "CellIndices",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        },
    )
    parent_grid_representation: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "ParentGridRepresentation",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        },
    )


@dataclass
class ColumnLayerParentWindow(AbstractParentWindow):
    """
    Parent window for any column-layer grid indexed as if it were an unstructured
    column layer grid, i.e., IJ columns are replaced by a column index.

    :ivar column_indices: Column indices that list the columns in the
        parent window. BUSINESS RULE: The ratio of fine to coarse column
        counts must be an integer for each coarse column.
    :ivar omit_parent_cells: List of parent cells that are to be
        retained at their original resolution and are not to be included
        within a local grid. The "omit" allows non-rectangular local
        grids to be specified. 0-based indexing follows #Columns x
        #Layers relative to the parent window cell count, not to the
        parent grid.
    :ivar kregrid:
    :ivar parent_column_layer_grid_representation:
    """

    column_indices: Optional[AbstractIntegerArray] = field(
        default=None,
        metadata={
            "name": "ColumnIndices",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        },
    )
    omit_parent_cells: Optional[AbstractIntegerArray] = field(
        default=None,
        metadata={
            "name": "OmitParentCells",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        },
    )
    kregrid: Optional[Regrid] = field(
        default=None,
        metadata={
            "name": "KRegrid",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        },
    )
    parent_column_layer_grid_representation: Optional[
        DataObjectReference
    ] = field(
        default=None,
        metadata={
            "name": "ParentColumnLayerGridRepresentation",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        },
    )


@dataclass
class ColumnLayerSubnodeTopology(SubnodeTopology):
    """
    This data-object consists of the unstructured cell finite elements subnode
    topology plus the column subnodes.
    """

    column_subnode_patch: List[ColumnSubnodePatch] = field(
        default_factory=list,
        metadata={
            "name": "ColumnSubnodePatch",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        },
    )


@dataclass
class GeologicUnitOccurrenceInterpretation(
    AbstractGeologicUnitOrganizationInterpretation
):
    """A local Interpretation—it could be along a well, on a 2D map, or on a 2D
    section or on a part of the global volume of an earth model—of a succession of
    rock feature elements. The stratigraphic column rank interpretation composing a
    stratigraphic occurrence can be ordered by the criteria listed in
    OrderingCriteria.

    Note: When the chosen ordering criterion is not age but measured depth along a well trajectory, the semantics of the name of this class could be inconsistent semantics. In this case:
    - When faults are present, the observed succession may show repetition of a stratigraphic succession composed of a series of units each younger than the one below it.
    - This succession should not be called a stratigraphic occurrence because it is not stratigraphic (because the adjective ‘stratigraphic’ applies to a succession of units ordered according to their relative ages).
    A more general term for designating a succession of geological units encountered in drilling would be "Geologic Occurrence". So we may consider that the term "stratigraphic cccurrence interpretation" should be understood as "geologic occurrence interpretation".
    """

    class Meta:
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"

    geologic_unit: List[DataObjectReference] = field(
        default_factory=list,
        metadata={
            "name": "GeologicUnit",
            "type": "Element",
        },
    )
    is_occurrence_of: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "IsOccurrenceOf",
            "type": "Element",
        },
    )


@dataclass
class IjkParentWindow(AbstractParentWindow):
    """
    Parent window for any IJK grid.

    :ivar omit_parent_cells: List of parent cells that are to be
        retained at their original resolution and are not to be included
        within a local grid. The "omit" allows non-rectangular local
        grids to be specified. 0-based indexing follows NI x NJ x NK
        relative to the parent window cell count—not to the parent grid.
    :ivar jregrid:
    :ivar parent_ijk_grid_representation:
    :ivar kregrid:
    :ivar iregrid:
    """

    omit_parent_cells: Optional[AbstractIntegerArray] = field(
        default=None,
        metadata={
            "name": "OmitParentCells",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        },
    )
    jregrid: Optional[Regrid] = field(
        default=None,
        metadata={
            "name": "JRegrid",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        },
    )
    parent_ijk_grid_representation: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "ParentIjkGridRepresentation",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        },
    )
    kregrid: Optional[Regrid] = field(
        default=None,
        metadata={
            "name": "KRegrid",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        },
    )
    iregrid: Optional[Regrid] = field(
        default=None,
        metadata={
            "name": "IRegrid",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        },
    )


@dataclass
class NonSealedSurfaceFrameworkRepresentation(
    AbstractSurfaceFrameworkRepresentation
):
    """A collection of contact representations parts, which are a list of contact
    patches with no identity.

    This collection of contact representations is completed by a set of
    representations gathered at the representation set representation
    level.
    """

    class Meta:
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"

    contacts: List[AbstractSurfaceFrameworkContact] = field(
        default_factory=list,
        metadata={
            "name": "Contacts",
            "type": "Element",
        },
    )


@dataclass
class PolylineSetRepresentation(AbstractRepresentation):
    """A representation made up of a set of polylines or a set of polygonal chains
    (for more information, see PolylineRepresentation).

    For compactness, it is organized by line patch as a unique polyline
    set patch. If allPolylineClosed = True, all the polylines are
    connected between the first and the last point. Its geometry is a 1D
    array of points, corresponding to the concatenation of the points of
    all polyline points.
    """

    class Meta:
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"

    line_role: Optional[Union[LineRole, str]] = field(
        default=None,
        metadata={
            "name": "LineRole",
            "type": "Element",
            "pattern": r".*:.*",
        },
    )
    line_patch: List[PolylineSetPatch] = field(
        default_factory=list,
        metadata={
            "name": "LinePatch",
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass
class ReservoirCompartmentUnitInterpretation:
    """
    A geologic unit or formation located within a reservoir compartment.
    """

    fluid_units: List[DataObjectReference] = field(
        default_factory=list,
        metadata={
            "name": "FluidUnits",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "max_occurs": 3,
        },
    )
    reservoir_compartment: Optional[
        ReservoirCompartmentInterpretation
    ] = field(
        default=None,
        metadata={
            "name": "ReservoirCompartment",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        },
    )
    geologic_unit_interpretation: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "GeologicUnitInterpretation",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        },
    )


@dataclass
class SealedSurfaceFrameworkRepresentation(
    AbstractSurfaceFrameworkRepresentation
):
    """A collection of contact representations parts, which are a list of contact
    patches and their identities.

    This collection of contact representations is completed by a set of
    representations gathered at the representation set representation
    level.
    """

    class Meta:
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"

    contacts: List[SealedContact] = field(
        default_factory=list,
        metadata={
            "name": "Contacts",
            "type": "Element",
        },
    )


@dataclass
class SeismicLatticeSetFeature(AbstractSeismicSurveyFeature):
    """An unordered set of several seismic lattices.

    Generally, it has no direct interpretation or representation.
    """


@dataclass
class SeismicLineSetFeature(AbstractSeismicSurveyFeature):
    """An unordered set of several seismic lines.

    Generally, it has no direct interpretation or representation.
    """

    class Meta:
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class StratigraphicColumnRankInterpretation(
    AbstractGeologicUnitOrganizationInterpretation
):
    """
    A global hierarchy containing an ordered list of stratigraphic unit
    interpretations.

    :ivar rank_in_stratigraphic_column: The rank in the stratigraphic
        column.
    :ivar stratigraphic_units:
    """

    class Meta:
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"

    rank_in_stratigraphic_column: Optional[int] = field(
        default=None,
        metadata={
            "name": "RankInStratigraphicColumn",
            "type": "Element",
            "required": True,
            "min_inclusive": 0,
        },
    )
    stratigraphic_units: List[DataObjectReference] = field(
        default_factory=list,
        metadata={
            "name": "StratigraphicUnits",
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass
class StreamlinesRepresentation(AbstractRepresentation):
    """Representation of streamlines associated with a streamline feature and
    interpretation.

    Use StreamlinesFeature to define the vector field that supports the streamlines, i.e., describes what flux is being traced.
    Use Interpretation to distinguish between shared and differing interpretations.
    Usage Note: When defining streamline geometry, the PatchIndex is not referenced and may be set to a value of 0.

    :ivar line_count: Number of streamlines.
    :ivar streamline_wellbores:
    :ivar geometry:
    """

    class Meta:
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"

    line_count: Optional[int] = field(
        default=None,
        metadata={
            "name": "LineCount",
            "type": "Element",
            "required": True,
            "min_inclusive": 1,
        },
    )
    streamline_wellbores: Optional[StreamlineWellbores] = field(
        default=None,
        metadata={
            "name": "StreamlineWellbores",
            "type": "Element",
        },
    )
    geometry: Optional[PolylineSetPatch] = field(
        default=None,
        metadata={
            "name": "Geometry",
            "type": "Element",
        },
    )


@dataclass
class TriangulatedSetRepresentation(AbstractSurfaceRepresentation):
    """A representation based on set of triangulated mesh patches, which gets its
    geometry from a 1D array of points.

    BUSINESS RULE: The orientation of all the triangles of this representation must be consistent.
    """

    class Meta:
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"

    triangle_patch: List[TrianglePatch] = field(
        default_factory=list,
        metadata={
            "name": "TrianglePatch",
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass
class UnstructuredSubnodeTopology(SubnodeTopology):
    """If edge subnodes are used, then edges must be defined.

    If cell subnodes are used, nodes per cell must be defined.
    """

    nodes_per_cell: Optional[JaggedArray] = field(
        default=None,
        metadata={
            "name": "NodesPerCell",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        },
    )
    edges: Optional[Edges] = field(
        default=None,
        metadata={
            "name": "Edges",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        },
    )


@dataclass
class VoidageGroupInterpretation(AbstractOrganizationInterpretation):
    """A group of ReservoirSegments which are hydraulically connected and are
    generally developed as a single reservoir.

    Membership in this organization can change over time (geologic and
    over the life of a field or interpretation activity) and is an
    interpretation.
    """

    stratigraphy: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "Stratigraphy",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        },
    )
    fluids: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "Fluids",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        },
    )
    compartments: List[ReservoirCompartmentInterpretation] = field(
        default_factory=list,
        metadata={
            "name": "Compartments",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        },
    )


@dataclass
class AbstractColumnLayerGridGeometry(AbstractGridGeometry):
    """Description of the geometry of a column layer grid, e.g., parity and pinch,
    together with its supporting topology.

    - Column layer grid cell geometry is based upon nodes on coordinate lines.
    - Geometry is contained within the representation of a grid.
    - Point Geometry is that of the column layer coordinate line nodes. Coordinate line nodes for all of the coordinate lines, with NKL nodes per line.
    - The numbering of these lines follow the pillar numbering if no split coordinate lines are present.
    - The unsplit coordinate lines share an indexing with the pillars. The numbering of the remaining lines are defined in the columnsPerSplitCoordinateLine list-of-lists if split coordinate lines are present.
    - Pillar numbering is either 1D or 2D, so for unfaulted grids, the node dimensions may follow either a 2D or 3D array. Otherwise the nodes will be 2D.
    - In HDF5 nodes are stored as separate X, Y, Z, values, so add another dimension (size=3) which is fastest in HDF5.

    :ivar cell_geometry_is_defined: Indicator that a cell has a defined
        geometry. This attribute is grid metadata. If the indicator
        shows that the cell geometry is NOT defined, then this attribute
        overrides any other node geometry specification. Array index is
        2D/3D.
    :ivar kdirection:
    :ivar node_is_colocated_in_kdirection: Optional indicator that two
        adjacent nodes on a coordinate line are colocated. This is
        considered grid metadata, and is intended to over-ride any
        geometric comparison of node locations. Array index follows
        #CoordinateLines x (NKL-1).
    :ivar node_is_colocated_on_kedge: Optional indicator that two
        adjacent nodes on the KEDGE of a cell are colocated. This is
        considered grid metadata, and is intended to over-ride any
        geometric comparison of node locations. Array index follows
        #EdgesPerColumn x NKL for unstructured column layer grids and 4
        x NI x NJ x NKL for IJK grids.
    :ivar pillar_geometry_is_defined: Indicator that a pillar has at
        least one node with a defined cell geometry. This is considered
        grid metadata. If the indicator does not indicate that the
        pillar geometry is defined, then this over-rides any other node
        geometry specification. Array index follows #Pillars and so may
        be either 2D or 1D.
    :ivar pillar_shape:
    :ivar split_column_edges:
    :ivar column_layer_subnode_topology:
    :ivar column_layer_split_coordinate_lines:
    :ivar split_node_patch:
    """

    cell_geometry_is_defined: Optional[AbstractBooleanArray] = field(
        default=None,
        metadata={
            "name": "CellGeometryIsDefined",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        },
    )
    kdirection: Optional[Kdirection] = field(
        default=None,
        metadata={
            "name": "KDirection",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        },
    )
    node_is_colocated_in_kdirection: Optional[AbstractBooleanArray] = field(
        default=None,
        metadata={
            "name": "NodeIsColocatedInKDirection",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        },
    )
    node_is_colocated_on_kedge: Optional[AbstractBooleanArray] = field(
        default=None,
        metadata={
            "name": "NodeIsColocatedOnKEdge",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        },
    )
    pillar_geometry_is_defined: Optional[AbstractBooleanArray] = field(
        default=None,
        metadata={
            "name": "PillarGeometryIsDefined",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        },
    )
    pillar_shape: Optional[PillarShape] = field(
        default=None,
        metadata={
            "name": "PillarShape",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        },
    )
    split_column_edges: Optional[SplitColumnEdges] = field(
        default=None,
        metadata={
            "name": "SplitColumnEdges",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        },
    )
    column_layer_subnode_topology: Optional[
        ColumnLayerSubnodeTopology
    ] = field(
        default=None,
        metadata={
            "name": "ColumnLayerSubnodeTopology",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        },
    )
    column_layer_split_coordinate_lines: Optional[
        ColumnLayerSplitCoordinateLines
    ] = field(
        default=None,
        metadata={
            "name": "ColumnLayerSplitCoordinateLines",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        },
    )
    split_node_patch: Optional[SplitNodePatch] = field(
        default=None,
        metadata={
            "name": "SplitNodePatch",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        },
    )


@dataclass
class AbstractColumnLayerGridRepresentation(AbstractGridRepresentation):
    """Abstract class that includes IJK grids and unstructured column layer grids.

    All column layer grids have a layer index K=1,...,NK or K0=0,...,NK-1.
    Cell geometry is characterized by nodes on coordinate lines.

    :ivar nk: Number of layers in the grid. Must be positive.
    """

    nk: Optional[int] = field(
        default=None,
        metadata={
            "name": "Nk",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
            "min_inclusive": 1,
        },
    )


@dataclass
class AbstractTruncatedColumnLayerGridRepresentation(
    AbstractGridRepresentation
):
    """Abstract class for truncated IJK grids and truncated unstructured column
    layer grids.

    Each column layer grid class must have a defined geometry in which
    cells are truncated and additional split cells are defined.

    :ivar nk: Number of layers in the grid. Must be positive.
    :ivar truncation_cell_patch:
    """

    nk: Optional[int] = field(
        default=None,
        metadata={
            "name": "Nk",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
            "min_inclusive": 1,
        },
    )
    truncation_cell_patch: Optional[TruncationCellPatch] = field(
        default=None,
        metadata={
            "name": "TruncationCellPatch",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        },
    )


@dataclass
class AdditionalGridTopology:
    """Additional grid topology and/or patches, if required, for indexable elements
    that otherwise do not have their topology defined within the grid
    representation.

    For example, column edges need to be defined if you want to have an
    enumeration for the faces of a column layer grid, but not otherwise.
    """

    split_edges: Optional[SplitEdges] = field(
        default=None,
        metadata={
            "name": "SplitEdges",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        },
    )
    split_node_patch: Optional[SplitNodePatch] = field(
        default=None,
        metadata={
            "name": "SplitNodePatch",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        },
    )
    split_column_edges: Optional[SplitColumnEdges] = field(
        default=None,
        metadata={
            "name": "SplitColumnEdges",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        },
    )
    unstructured_column_edges: Optional[UnstructuredColumnEdges] = field(
        default=None,
        metadata={
            "name": "UnstructuredColumnEdges",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        },
    )
    split_faces: Optional[SplitFaces] = field(
        default=None,
        metadata={
            "name": "SplitFaces",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        },
    )
    unstructured_subnode_topology: Optional[
        UnstructuredSubnodeTopology
    ] = field(
        default=None,
        metadata={
            "name": "UnstructuredSubnodeTopology",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        },
    )
    column_layer_subnode_topology: Optional[
        ColumnLayerSubnodeTopology
    ] = field(
        default=None,
        metadata={
            "name": "ColumnLayerSubnodeTopology",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        },
    )


@dataclass
class CmpLineFeature(AbstractSeismicLineFeature):
    """
    Location of a single line of common mid-points (CMP) resulting from a 2D
    seismic acquisition.

    :ivar nearest_shot_point_indices: Index of closest shot point
        (inside the associated CmpPointLineFeature) for each cmp.
    :ivar shot_point_line_feature:
    """

    class Meta:
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"

    nearest_shot_point_indices: Optional[AbstractIntegerArray] = field(
        default=None,
        metadata={
            "name": "NearestShotPointIndices",
            "type": "Element",
            "required": True,
        },
    )
    shot_point_line_feature: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "ShotPointLineFeature",
            "type": "Element",
        },
    )


@dataclass
class Seismic3DPostStackRepresentation(AbstractGridRepresentation):
    """The feature of this representation should be the same survey feature as the
    associated Grid2Representation represents.

    The indexing convention (mainly for associated properties) is:
    - Trace sample goes fastest
    - Then inline
    - And crossline goes slowest
    The indexing convention only applies to HDF datasets (not SEGY file).
    A whole SEGY file can be referenced in properties of this representation, but not partial files.

    :ivar seismic_lattice_sub_sampling: This array must be two
        dimensions: - Fastest Axis is inline. - Slowest Axis is
        crossline. The index is based on array indexing, not on index
        labeling of inlines/crosslines. The values of the integer
        lattice array are the increments between 2 consecutive
        subsampled nodes.
    :ivar trace_sampling: Defines the sampling in the vertical dimension
        of the representation. This array must be one dimension. The
        values are given with respect to the associated Local Crs.
    :ivar seismic_lattice_representation:
    :ivar local_crs:
    """

    class Meta:
        name = "Seismic3dPostStackRepresentation"
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"

    seismic_lattice_sub_sampling: Optional[IntegerLatticeArray] = field(
        default=None,
        metadata={
            "name": "SeismicLatticeSubSampling",
            "type": "Element",
            "required": True,
        },
    )
    trace_sampling: Optional[FloatingPointLatticeArray] = field(
        default=None,
        metadata={
            "name": "TraceSampling",
            "type": "Element",
            "required": True,
        },
    )
    seismic_lattice_representation: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "SeismicLatticeRepresentation",
            "type": "Element",
            "required": True,
        },
    )
    local_crs: Optional[DataObjectReference] = field(
        default=None,
        metadata={
            "name": "LocalCrs",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class SeismicLatticeFeature(AbstractSeismicSurveyFeature):
    """Defined by two lateral ordered dimensions: inline (lateral), crossline (lateral and orthogonal to the inline dimension), which are fixed.
    To specify its location, a seismic feature can be associated with the seismic coordinates of the points of a representation.
    Represented by a 2D grid representation.

    :ivar crossline_labels: The labels (as they would be found in SEGY
        trace headers for example) of the crosslines of the 3D seismic
        survey. BUSINESS RULE: Count of this array must be the same as
        the count of nodes in the slowest axis of the associated grid 2D
        representations.
    :ivar inline_labels: The labels (as they would be found in SEGY
        trace headers for example) of the inlines of the 3D seismic
        survey. BUSINESS RULE: Count of this array must be the same as
        the count of nodes in the fastest axis of the associated grid 2D
        representations.
    :ivar is_part_of:
    """

    class Meta:
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"

    crossline_labels: Optional[IntegerLatticeArray] = field(
        default=None,
        metadata={
            "name": "CrosslineLabels",
            "type": "Element",
        },
    )
    inline_labels: Optional[IntegerLatticeArray] = field(
        default=None,
        metadata={
            "name": "InlineLabels",
            "type": "Element",
        },
    )
    is_part_of: Optional[SeismicLatticeSetFeature] = field(
        default=None,
        metadata={
            "name": "IsPartOf",
            "type": "Element",
        },
    )


@dataclass
class ShotPointLineFeature(AbstractSeismicLineFeature):
    """
    Location of a single line of shot points in a 2D seismic acquisition.
    """

    class Meta:
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"


@dataclass
class UnstructuredGridGeometry(AbstractGridGeometry):
    """Description of the geometry of an unstructured cell grid, which includes
    geometric characteristics, e.g., cell face parity, and supporting topology.

    Each grid cell is defined by a (signed) list of cell faces. Each
    cell face is defined by a list of nodes.

    :ivar cell_face_is_right_handed: Boolean mask used to indicate which
        cell faces have an outwardly directed normal following a right
        hand rule. Array length is the sum of the cell face count per
        cell, and the data follows the order of the faces per cell
        RESQMLlist-of-lists.
    :ivar cell_shape:
    :ivar face_count: Total number of faces in the grid. Must be
        positive.
    :ivar faces_per_cell: List of faces per cell. Face count per cell
        can be obtained from the offsets in the first list-of-lists
        array. BUSINESS RULE: CellCount must match the length of the
        first list-of-lists array.
    :ivar node_count: Total number of nodes in the grid. Must be
        positive.
    :ivar nodes_per_face: List of nodes per face. Node count per face
        can be obtained from the offsets in the first list-of-lists
        array. BUSINESS RULE: FaceCount must match the length of the
        first list- of-lists array.
    :ivar unstructured_grid_hinge_node_faces:
    :ivar unstructured_subnode_topology:
    """

    cell_face_is_right_handed: Optional[AbstractBooleanArray] = field(
        default=None,
        metadata={
            "name": "CellFaceIsRightHanded",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        },
    )
    cell_shape: Optional[CellShape] = field(
        default=None,
        metadata={
            "name": "CellShape",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        },
    )
    face_count: Optional[int] = field(
        default=None,
        metadata={
            "name": "FaceCount",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
            "min_inclusive": 1,
        },
    )
    faces_per_cell: Optional[JaggedArray] = field(
        default=None,
        metadata={
            "name": "FacesPerCell",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        },
    )
    node_count: Optional[int] = field(
        default=None,
        metadata={
            "name": "NodeCount",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
            "min_inclusive": 1,
        },
    )
    nodes_per_face: Optional[JaggedArray] = field(
        default=None,
        metadata={
            "name": "NodesPerFace",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        },
    )
    unstructured_grid_hinge_node_faces: Optional[
        UnstructuredGridHingeNodeFaces
    ] = field(
        default=None,
        metadata={
            "name": "UnstructuredGridHingeNodeFaces",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        },
    )
    unstructured_subnode_topology: Optional[
        UnstructuredSubnodeTopology
    ] = field(
        default=None,
        metadata={
            "name": "UnstructuredSubnodeTopology",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        },
    )


@dataclass
class IjkGridGeometry(AbstractColumnLayerGridGeometry):
    """Explicit geometry definition for the cells of the IJK grid.

    Grid options are also defined through this data-object.

    :ivar grid_is_righthanded: Indicates that the IJK grid is right
        handed, as determined by the triple product of tangent vectors
        in the I, J, and K directions.
    :ivar ij_gaps:
    """

    grid_is_righthanded: Optional[bool] = field(
        default=None,
        metadata={
            "name": "GridIsRighthanded",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        },
    )
    ij_gaps: Optional[IjGaps] = field(
        default=None,
        metadata={
            "name": "IjGaps",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        },
    )


@dataclass
class RepresentationIdentity:
    """Indicates the nature of the relationship between 2 or more representations,
    specifically if they are partially or totally identical.

    For possible types of relationships, see IdentityKind.

    :ivar identical_element_count: Number of elements within each
        representation for which a representation identity is specified.
    :ivar element_identity:
    :ivar additional_grid_topology:
    """

    identical_element_count: Optional[int] = field(
        default=None,
        metadata={
            "name": "IdenticalElementCount",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
            "min_inclusive": 1,
        },
    )
    element_identity: List[ElementIdentity] = field(
        default_factory=list,
        metadata={
            "name": "ElementIdentity",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "min_occurs": 2,
        },
    )
    additional_grid_topology: Optional[AdditionalGridTopology] = field(
        default=None,
        metadata={
            "name": "AdditionalGridTopology",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        },
    )


@dataclass
class SubRepresentation(AbstractRepresentation):
    """An ordered list of indexable elements and/or indexable element pairs of an
    existing representation.

    Because the representation concepts of topology, geometry, and
    property values are separate in RESQML, it is now possible to select
    a range of nodes, edges, faces, or volumes (cell) indices from the
    topological support of an existing representation to define a sub-
    representation. A sub-representation may describe a different
    feature interpretation using the same geometry or property as the
    "parent" representation. In this case, the only information
    exchanged is a set of potentially non-consecutive indices of the
    topological support of the representation. Optional additional grid
    topology is available for grid representations.
    """

    class Meta:
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"

    indexable_element: Optional[IndexableElement] = field(
        default=None,
        metadata={
            "name": "IndexableElement",
            "type": "Element",
            "required": True,
        },
    )
    additional_grid_topology: Optional[AdditionalGridTopology] = field(
        default=None,
        metadata={
            "name": "AdditionalGridTopology",
            "type": "Element",
        },
    )
    sub_representation_patch: List[SubRepresentationPatch] = field(
        default_factory=list,
        metadata={
            "name": "SubRepresentationPatch",
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass
class UnstructuredColumnLayerGridGeometry(AbstractColumnLayerGridGeometry):
    """Description of the geometry of an unstructured column-layer grid, e.g.,
    parity and pinch, together with its supporting topology.

    Unstructured column-layer cell geometry is derived from column-layer
    cell geometry and hence is based upon nodes on coordinate lines.
    Geometry is contained within the representation of a grid.

    :ivar column_is_right_handed: List of columns that are right handed.
        Right handedness is evaluated following the pillar order and the
        K-direction tangent vector for each column.
    :ivar column_shape:
    :ivar pillar_count: Number of pillars in the grid. Must be positive.
        Pillars are used to describe the shape of the columns in the
        grid.
    :ivar pillars_per_column: List of pillars for each column. The
        pillars define the corners of each column. The number of pillars
        per column can be obtained from the offsets in the first list-
        of-lists array. BUSINESS RULE: The length of the first array in
        the list -of-lists construction must equal the columnCount.
    :ivar unstructured_column_edges:
    """

    column_is_right_handed: Optional[AbstractBooleanArray] = field(
        default=None,
        metadata={
            "name": "ColumnIsRightHanded",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        },
    )
    column_shape: Optional[ColumnShape] = field(
        default=None,
        metadata={
            "name": "ColumnShape",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        },
    )
    pillar_count: Optional[int] = field(
        default=None,
        metadata={
            "name": "PillarCount",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
            "min_inclusive": 1,
        },
    )
    pillars_per_column: Optional[JaggedArray] = field(
        default=None,
        metadata={
            "name": "PillarsPerColumn",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
        },
    )
    unstructured_column_edges: Optional[UnstructuredColumnEdges] = field(
        default=None,
        metadata={
            "name": "UnstructuredColumnEdges",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        },
    )


@dataclass
class UnstructuredGpGridPatch:
    """Used to specify unstructured cell grid patch(es) within a general purpose
    grid.

    Multiple patches are supported.

    :ivar unstructured_cell_count: Number of unstructured cells.
        Degenerate case (count=0) is allowed for GPGrid.
    :ivar geometry:
    """

    unstructured_cell_count: Optional[int] = field(
        default=None,
        metadata={
            "name": "UnstructuredCellCount",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
            "min_inclusive": 0,
        },
    )
    geometry: Optional[UnstructuredGridGeometry] = field(
        default=None,
        metadata={
            "name": "Geometry",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        },
    )


@dataclass
class UnstructuredGridRepresentation(AbstractGridRepresentation):
    """Unstructured grid representation characterized by a cell count, and
    potentially nothing else.

    Both the oldest and newest simulation formats are based on this
    format.

    :ivar cell_count: Number of cells in the grid. Must be positive.
    :ivar original_cell_index:
    :ivar geometry:
    """

    class Meta:
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"

    cell_count: Optional[int] = field(
        default=None,
        metadata={
            "name": "CellCount",
            "type": "Element",
            "required": True,
            "min_inclusive": 1,
        },
    )
    original_cell_index: Optional[AlternateCellIndex] = field(
        default=None,
        metadata={
            "name": "OriginalCellIndex",
            "type": "Element",
        },
    )
    geometry: Optional[UnstructuredGridGeometry] = field(
        default=None,
        metadata={
            "name": "Geometry",
            "type": "Element",
        },
    )


@dataclass
class IjkGpGridPatch:
    """Used to specify IJK grid patch(es) within a general purpose grid.

    Multiple patches are supported.

    :ivar ni: Count of I indices. Degenerate case (ni=0) is allowed for
        GPGrid representations.
    :ivar nj: Count of J indices. Degenerate case (nj=0) is allowed for
        GPGrid representations.
    :ivar radial_grid_is_complete: TRUE if the grid is periodic in J,
        i.e., has the topology of a complete 360 degree circle. If TRUE,
        then NJL=NJ. Otherwise, NJL=NJ+1
    :ivar geometry:
    :ivar truncation_cell_patch:
    """

    ni: Optional[int] = field(
        default=None,
        metadata={
            "name": "Ni",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
            "min_inclusive": 0,
        },
    )
    nj: Optional[int] = field(
        default=None,
        metadata={
            "name": "Nj",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
            "min_inclusive": 0,
        },
    )
    radial_grid_is_complete: Optional[bool] = field(
        default=None,
        metadata={
            "name": "RadialGridIsComplete",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        },
    )
    geometry: Optional[IjkGridGeometry] = field(
        default=None,
        metadata={
            "name": "Geometry",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        },
    )
    truncation_cell_patch: Optional[TruncationCellPatch] = field(
        default=None,
        metadata={
            "name": "TruncationCellPatch",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        },
    )


@dataclass
class IjkGridRepresentation(AbstractColumnLayerGridRepresentation):
    """Grid whose topology is characterized by structured column indices (I,J) and
    a layer index, K. Cell geometry is characterized by nodes on coordinate lines,
    where each column of the model has 4 sides. Geometric degeneracy is permitted.

    IJK grids support the following specific extensions:
    - IJK radial grids
    - K-Layer gaps
    - IJ-Column gaps

    :ivar ni: Count of cells in the I-direction in the grid. Must be
        positive. I=1,...,NI, I0=0,...,NI-1.
    :ivar nj: Count of cells in the J-direction in the grid. Must be
        positive. J=1,...,NJ, J0=0,...,NJ-1.
    :ivar radial_grid_is_complete: TRUE if the grid is periodic in J,
        i.e., has the topology of a complete 360 degree circle. If TRUE,
        then NJL=NJ. Otherwise, NJL=NJ+1 May be used to change the grid
        topology for either a Cartesian or a radial grid, although
        radial grid usage is by far the more common.
    :ivar kgaps:
    :ivar geometry:
    """

    class Meta:
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"

    ni: Optional[int] = field(
        default=None,
        metadata={
            "name": "Ni",
            "type": "Element",
            "required": True,
            "min_inclusive": 1,
        },
    )
    nj: Optional[int] = field(
        default=None,
        metadata={
            "name": "Nj",
            "type": "Element",
            "required": True,
            "min_inclusive": 1,
        },
    )
    radial_grid_is_complete: Optional[bool] = field(
        default=None,
        metadata={
            "name": "RadialGridIsComplete",
            "type": "Element",
        },
    )
    kgaps: Optional[Kgaps] = field(
        default=None,
        metadata={
            "name": "KGaps",
            "type": "Element",
        },
    )
    geometry: Optional[IjkGridGeometry] = field(
        default=None,
        metadata={
            "name": "Geometry",
            "type": "Element",
        },
    )


@dataclass
class RepresentationIdentitySet(AbstractObject):
    """
    A collection of representation identities.
    """

    class Meta:
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"

    representation_identity: List[RepresentationIdentity] = field(
        default_factory=list,
        metadata={
            "name": "RepresentationIdentity",
            "type": "Element",
            "min_occurs": 1,
        },
    )


@dataclass
class TruncatedIjkGridRepresentation(
    AbstractTruncatedColumnLayerGridRepresentation
):
    """Grid class with an underlying IJK topology, together with a 1D split-cell
    list.

    The truncated IJK cells have more than the usual 6 faces. The split
    cells are arbitrary polyhedra, identical to those of an unstructured
    cell grid.

    :ivar ni: Count of I-indices in the grid. Must be positive.
    :ivar nj: Count of J-indices in the grid. Must be positive.
    :ivar geometry:
    """

    class Meta:
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"

    ni: Optional[int] = field(
        default=None,
        metadata={
            "name": "Ni",
            "type": "Element",
            "required": True,
            "min_inclusive": 1,
        },
    )
    nj: Optional[int] = field(
        default=None,
        metadata={
            "name": "Nj",
            "type": "Element",
            "required": True,
            "min_inclusive": 1,
        },
    )
    geometry: Optional[IjkGridGeometry] = field(
        default=None,
        metadata={
            "name": "Geometry",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class TruncatedUnstructuredColumnLayerGridRepresentation(
    AbstractTruncatedColumnLayerGridRepresentation
):
    """Grid class with an underlying unstructured column-layer topology, together
    with a 1D split-cell list.

    The truncated cells have more than the usual number of faces within
    each column. The split cells are arbitrary polyhedra, identical to
    those of an unstructured cell grid.

    :ivar column_count: Number of unstructured columns in the grid. Must
        be positive.
    :ivar geometry:
    """

    class Meta:
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"

    column_count: Optional[int] = field(
        default=None,
        metadata={
            "name": "ColumnCount",
            "type": "Element",
            "required": True,
            "min_inclusive": 1,
        },
    )
    geometry: Optional[UnstructuredColumnLayerGridGeometry] = field(
        default=None,
        metadata={
            "name": "Geometry",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class UnstructuredColumnLayerGpGridPatch:
    """Used to specify unstructured column-layer grid patch(es) within a general
    purpose grid.

    Multiple patches are supported.

    :ivar unstructured_column_count: Number of unstructured columns.
        Degenerate case (count=0) is allowed for GPGrid.
    :ivar geometry:
    :ivar truncation_cell_patch:
    """

    unstructured_column_count: Optional[int] = field(
        default=None,
        metadata={
            "name": "UnstructuredColumnCount",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
            "min_inclusive": 0,
        },
    )
    geometry: Optional[UnstructuredColumnLayerGridGeometry] = field(
        default=None,
        metadata={
            "name": "Geometry",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        },
    )
    truncation_cell_patch: Optional[TruncationCellPatch] = field(
        default=None,
        metadata={
            "name": "TruncationCellPatch",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        },
    )


@dataclass
class UnstructuredColumnLayerGridRepresentation(
    AbstractColumnLayerGridRepresentation
):
    """Grid whose topology is characterized by an unstructured column index and a
    layer index, K.

    Cell geometry is characterized by nodes on coordinate lines, where
    each column of the model may have an arbitrary number of sides.

    :ivar column_count: Number of unstructured columns in the grid. Must
        be positive.
    :ivar geometry:
    """

    class Meta:
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"

    column_count: Optional[int] = field(
        default=None,
        metadata={
            "name": "ColumnCount",
            "type": "Element",
            "required": True,
            "min_inclusive": 1,
        },
    )
    geometry: Optional[UnstructuredColumnLayerGridGeometry] = field(
        default=None,
        metadata={
            "name": "Geometry",
            "type": "Element",
        },
    )


@dataclass
class ColumnLayerGpGrid:
    """Used to construct a column layer grid patch based upon multiple unstructured
    column-layer and IJK grids that share a layering scheme.

    Multiple patches are supported.

    :ivar nk: Number of layers. Degenerate case (nk=0) is allowed for
        GPGrid.
    :ivar kgaps:
    :ivar ijk_gp_grid_patch:
    :ivar unstructured_column_layer_gp_grid_patch:
    """

    nk: Optional[int] = field(
        default=None,
        metadata={
            "name": "Nk",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
            "required": True,
            "min_inclusive": 0,
        },
    )
    kgaps: Optional[Kgaps] = field(
        default=None,
        metadata={
            "name": "KGaps",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        },
    )
    ijk_gp_grid_patch: List[IjkGpGridPatch] = field(
        default_factory=list,
        metadata={
            "name": "IjkGpGridPatch",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        },
    )
    unstructured_column_layer_gp_grid_patch: List[
        UnstructuredColumnLayerGpGridPatch
    ] = field(
        default_factory=list,
        metadata={
            "name": "UnstructuredColumnLayerGpGridPatch",
            "type": "Element",
            "namespace": "http://www.energistics.org/energyml/data/resqmlv2",
        },
    )


@dataclass
class GpGridRepresentation(AbstractGridRepresentation):
    """General purpose (GP) grid representation, which includes and/or extends the
    features from all other grid representations.

    This general purpose representation is included in the schema for
    research and/or advanced modeling purposes, but is not expected to
    be used for routine data transfer.
    """

    class Meta:
        namespace = "http://www.energistics.org/energyml/data/resqmlv2"

    column_layer_gp_grid: List[ColumnLayerGpGrid] = field(
        default_factory=list,
        metadata={
            "name": "ColumnLayerGpGrid",
            "type": "Element",
        },
    )
    unstructured_gp_grid_patch: List[UnstructuredGpGridPatch] = field(
        default_factory=list,
        metadata={
            "name": "UnstructuredGpGridPatch",
            "type": "Element",
        },
    )
